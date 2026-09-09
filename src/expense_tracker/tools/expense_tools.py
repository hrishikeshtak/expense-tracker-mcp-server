from fastmcp import FastMCP
from typing import Dict, Any

from expense_tracker.services.expense_service import ExpenseService
from expense_tracker.repositories.expense_repository import ExpenseRepository


def register_expense_tools(mcp: FastMCP) -> None:
    """Register Expense tools"""

    service = ExpenseService(ExpenseRepository)

    @mcp.tool
    def add_expense(
        date: str,
        amount: float,
        category: str,
        sub_category: str = "",
        notes: str = "",
    ) -> Dict[str, Any]:
        """Add an expense to the expense tracker."""

        return service.add_expense(
            date=date,
            amount=amount,
            category=category,
            sub_category=sub_category,
            notes=notes,
        )

    @mcp.tool
    def list_expenses() -> list[dict[str, Any]]:
        """List all expenses."""

        return service.list_expenses()
