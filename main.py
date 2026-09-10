from fastmcp import FastMCP
from typing import Dict, Any, List
from src.expense_tracker.database.sqlite import init_db

init_db()

mcp = FastMCP(name="Expense Tracker")
init_db()

@mcp.tool
def add_expense(date: str, amount: float, category: str, sub_category: str = '', notes: str = '') -> Dict[str, Any]:
    """Add an expense to the database"""
    try:
        with connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO expenses (date, amount, category, sub_category, notes)
                VALUES (?, ?, ?, ?, ?)
            """, (date, amount, category, sub_category, notes))
            conn.commit()
            return {"status": "ok", "id": cursor.lastrowid, "message": "Expense added successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e), "id": None}
    finally:
        conn.close()

@mcp.tool
def list_expenses() -> List[Dict[str, Any]]:
    """List expenses from the database"""
    try:
        with connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, date, amount, category, sub_category, notes FROM expenses ORDER BY id ASC
            """)
            cols = [desc[0] for desc in cursor.description]
            expenses = [dict(zip(cols, row)) for row in cursor.fetchall()]
            return expenses
    finally:
        conn.close()
