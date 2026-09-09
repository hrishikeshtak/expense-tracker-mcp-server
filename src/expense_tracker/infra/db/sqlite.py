"""SQLite database implementation"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[4] / "expense.db"


def get_connection() -> sqlite3.Connection:
    """Get a connection to the database"""
    return sqlite3.connect(DB_PATH)


def init_db() -> None:
    """Initialize the database"""
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                sub_category TEXT DEFAULT '',
                notes TEXT DEFAULT ''
            )
            """
        )
    print("DB Initialized successfully!")

