"""Expense Tracker Service"""
from typing import Any, Dict, List


class ExpenseService:
    """Expense Tracker Service"""

    def __init__(self, expense_repository):
        self.repository = expense_repository

    def add_expense(
        self,
        date: str,
        amount: float,
        category: str,
        sub_category: str = "",
        notes: str = "",
    ) -> dict[str, Any]:
        """Add an expense to the database"""

        if amount <= 0:
            return {
                "status": "error",
                "message": "Amount must be greater than zero",
                "id": None,
            }

        expense_id = self.repository.add_expense(
            date=date,
            amount=amount,
            category=category,
            sub_category=sub_category,
            notes=notes,
        )

        return {
            "status": "ok",
            "id": expense_id,
            "message": "Expense added successfully",
        }

    def list_expenses(self) -> List[Dict[str, Any]]:
        """List expenses from the database"""
        return self.repository.list_expenses()
