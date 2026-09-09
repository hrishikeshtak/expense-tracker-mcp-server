from fastmcp import FastMCP

from expense_tracker.tools.expense_tools import register_expense_tools
from expense_tracker.infra.db.sqlite import init_db

init_db()

mcp = FastMCP(name="Expense Tracker")

register_expense_tools(mcp)
