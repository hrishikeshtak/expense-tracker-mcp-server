"""Expense repository implementation"""

from sqlite3 import Error
from typing import List, Dict, Any

from expense_tracker.infra.db.sqlite import get_connection


class ExpenseRepository:
    """Expense repository"""

    @staticmethod
    def add_expense(
        date: str,
        amount: float,
        category: str,
        sub_category: str = "",
        notes: str = "",
    ) -> int:
        """Add an expense to the database"""
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO expenses
                    (date, amount, category, sub_category, notes)
                VALUES (?, ?, ?, ?, ?)
                """,
                (date, amount, category, sub_category, notes),
            )
            return cursor.lastrowid

    @staticmethod
    def list_expenses() -> List[Dict[str, Any]]:
        """List expenses from the database"""
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT
                    id,
                    date,
                    amount,
                    category,
                    sub_category,
                    notes
                FROM expenses
                ORDER BY id ASC
                """
            )

            columns = [description[0] for description in cursor.description]

            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
