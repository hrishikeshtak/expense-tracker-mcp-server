# Expense Tracker MCP Server

An **MCP (Model Context Protocol) server for tracking daily expenses**.

The server provides MCP tools that allow an MCP-compatible client, such as Claude Desktop, to add and retrieve expenses using natural language.

The application currently uses **SQLite3** as its local persistence layer.

---

## Features

* Add daily expenses
* List all recorded expenses
* Categorize expenses using categories and sub-categories
* Add optional notes to expenses
* Persist expense data using SQLite3
* Test MCP tools using FastMCP Inspector
* Integrate with Claude Desktop

---

## Prerequisites

Make sure the following tools are installed:

* Python 3.12+
* [uv](https://docs.astral.sh/uv/)
* Node.js
* FastMCP

### Install Node.js

On macOS:

```bash
brew install node
```

---

## Project Setup

### 1. Initialize the project

```bash
uv init
```

### 2. Create a virtual environment

```bash
uv venv .
```

Activate the virtual environment if required:

```bash
source .venv/bin/activate
```

---

## Running the MCP Server

The MCP server is implemented in:

src/expense_tracker/server.py

### Run with FastMCP Inspector

FastMCP Inspector can be used to interactively test and debug the available MCP tools.

```bash
uv run fastmcp dev inspector src/expense_tracker/server.py
```

### Run the MCP Server

```bash
uv run fastmcp run src/expense_tracker/server.py
```

---

# Database

The Expense Tracker MCP Server currently uses **SQLite3** as its persistence layer.

SQLite is a good fit for the current application because the expense tracker is designed as a lightweight, local application and does not require a separate database server.


The database is automatically initialized when the MCP server starts.


## Expense Schema

The `expenses` table currently contains the following fields:

| Field          | Type    | Description                              | Required |
| -------------- | ------- | ---------------------------------------- | -------- |
| `id`           | INTEGER | Auto-generated unique expense ID         | Yes      |
| `date`         | TEXT    | Date of the expense                      | Yes      |
| `amount`       | REAL    | Expense amount                           | Yes      |
| `category`     | TEXT    | Main expense category                    | Yes      |
| `sub_category` | TEXT    | Expense sub-category                     | No       |
| `notes`        | TEXT    | Additional information about the expense | No       |

### Example Record

```text
id:           1
date:         2026-09-08
amount:       500.00
category:     Food
sub_category: Dinner
notes:        Dinner with family
```

---

# MCP Tools

The Expense Tracker MCP Server currently exposes the following MCP tools:

| Tool            | Description                               |
| --------------- | ----------------------------------------- |
| `add_expense`   | Adds a new expense to the SQLite database |
| `list_expenses` | Retrieves all expenses from the database  |

---

## `add_expense`

Adds a new expense to the `expenses` table.


### Example

A user can interact with the MCP server using natural language:

```text
Add an expense of ₹500 for dinner today.
```

The MCP client can invoke:

```python
add_expense(
    date="2026-09-08",
    amount=500,
    category="Food",
    sub_category="Dinner",
    notes=""
)
```

### Response

A successful request returns:

```json
{
    "status": "ok",
    "id": 1,
    "message": "Expense added successfully"
}
```

If an error occurs:

```json
{
    "status": "error",
    "message": "error message",
    "id": null
}
```

---

## `list_expenses`

Retrieves all expenses stored in the SQLite database.

The expenses are returned in ascending order of their database ID.

### Example

User request:

```text
Show me all my expenses.
```

The MCP client invokes:

```python
list_expenses()
```

### Response

Example:

```json
[
    {
        "id": 1,
        "date": "2026-09-08",
        "amount": 500.0,
        "category": "Food",
        "sub_category": "Dinner",
        "notes": "Dinner with family"
    },
    {
        "id": 2,
        "date": "2026-09-08",
        "amount": 120.0,
        "category": "Transport",
        "sub_category": "Cab",
        "notes": ""
    }
]
```

---

# MCP Architecture

The current architecture is intentionally simple:

```text
┌─────────────────────┐
│     MCP Client      │
│  Claude / Inspector │
└──────────┬──────────┘
           │
           │ MCP
           ▼
┌─────────────────────┐
│   FastMCP Server    │
│      main.py        │
├─────────────────────┤
│     MCP Tools       │
│                     │
│  add_expense()      │
│  list_expenses()    │
└──────────┬──────────┘
           │
           │ SQL
           ▼
┌─────────────────────┐
│      SQLite3        │
│                     │
│    expense.db       │
│                     │
│    expenses table   │
└─────────────────────┘
```

### Request Flow

For example, when a user asks:

```text
Add ₹250 for lunch today.
```

The flow is:

```text
User
  │
  ▼
MCP Client
  │
  ▼
add_expense()
  │
  ▼
SQLite
  │
  ▼
expense.db
```

For retrieving expenses:

```text
User
  │
  ▼
MCP Client
  │
  ▼
list_expenses()
  │
  ▼
SQLite
  │
  ▼
Expense Records
  │
  ▼
MCP Client
  │
  ▼
User
```

---

# Claude Desktop Integration

The MCP server can be integrated with Claude Desktop.

## Option 1: Install using FastMCP

FastMCP provides a convenient way to install the MCP server into Claude Desktop.

Run:

```bash
uv run fastmcp install claude-desktop src/expense_tracker/server.py
```

However, when using a Python project with a src/ layout, Claude Desktop may not automatically resolve the expense_tracker package correctly.

In that case, configure Claude Desktop to launch the server through uv.

## Option 2: Configure Claude Desktop using uv

Open the Claude Desktop MCP configuration file:

~/Library/Application Support/Claude/claude_desktop_config.json

Add the following configuration under mcpServers:

```
{
  "mcpServers": {
    "Expense Tracker": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/Users/hrishikeshtak/Developer/Git/mcp_servers/expense-tracker-mcp-server",
        "fastmcp",
        "run",
        "src/expense_tracker/server.py"
      ],
      "env": {},
      "transport": "stdio",
      "type": null,
      "cwd": null,
      "timeout": null,
      "keep_alive": null,
      "description": null,
      "icon": null,
      "authentication": null
    }
  }
```

### Important

Update:

/Users/hrishikeshtak/Developer/Git/mcp_servers/expense-tracker-mcp-server

to the absolute path of your local project directory.

The --directory option is important because it tells uv which project to run from. This allows uv to correctly resolve the project's virtual environment, dependencies, and src/expense_tracker package.

## Restart Claude Desktop

After updating the configuration:

1. Save claude_desktop_config.json.
2. Completely quit Claude Desktop.
3. Start Claude Desktop again.
4. Open the MCP/Connectors section.
5. Verify that Expense Tracker is running.
6. Verify that the available tools are displayed.

You should see:

Expense Tracker     
├── add_expense   
└── list_expenses

You can then interact with the server using natural language.

### Example Conversations

```text
Add ₹500 for dinner today.
```

```text
Add ₹120 for Uber under Transport.
```

```text
Show me all my expenses.
```

---

# Development Workflow

A typical development workflow is:

```text
        ┌──────────────────┐
        │  Develop MCP Tool │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ FastMCP Inspector │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │    Test Tools    │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Run MCP Server   │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │  Claude Desktop  │
        └──────────────────┘
```

---

# Useful Commands

| Purpose                    | Command                                         |
| -------------------------- | ----------------------------------------------- |
| Initialize project         | `uv init`                                       |
| Create virtual environment | `uv venv .`                                     |
| Install Node.js            | `brew install node`                             |
| Run FastMCP Inspector      | `uv run fastmcp dev inspector main.py`          |
| Run MCP server             | `uv run fastmcp run main.py`                    |
| Install in Claude Desktop  | `uv run fastmcp install claude-desktop main.py` |

---

# Future Enhancements

The current implementation provides basic expense creation and retrieval. Potential future MCP tools include:

* `update_expense` — Update an existing expense
* `delete_expense` — Delete an expense
* `get_expense` — Retrieve a specific expense
* `search_expenses` — Search expenses by keyword
* `get_expenses_by_date` — Filter expenses by date
* `get_expenses_by_category` — Filter expenses by category
* `get_expense_summary` — Calculate spending summaries
* `get_monthly_report` — Generate monthly expense reports
* `get_category_summary` — Analyze spending by category
* Budget tracking and alerts

As the application grows beyond a local/single-user use case, SQLite could potentially be replaced with a server-based database such as PostgreSQL.
