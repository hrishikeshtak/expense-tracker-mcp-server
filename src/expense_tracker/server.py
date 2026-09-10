from fastmcp import FastMCP

from expense_tracker.infra.db.sqlite import init_db
from expense_tracker.tools.expense_tools import register_expense_tools


mcp = FastMCP(name="Expense Tracker")

init_db()
register_expense_tools(mcp)
