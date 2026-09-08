# Expense Tracker MCP Server

An **MCP (Model Context Protocol) server for tracking daily expenses**. It allows an MCP-compatible client such as Claude Desktop to interact with an expense tracker through natural language.

## Features

* Track daily expenses
* Add and manage expense records
* Query expenses through natural language
* Integrate with MCP-compatible clients
* Run and test the server locally using FastMCP Inspector
* Integrate with Claude Desktop

## Prerequisites

Make sure the following tools are installed:

* [Python](https://www.python.org/)
* [uv](https://docs.astral.sh/uv/)
* [Node.js](https://nodejs.org/)
* FastMCP

### Install Node.js

On macOS:

```bash
brew install node
```

## Project Setup

### 1. Initialize the project

Create and initialize the Python project using `uv`:

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

Install the project dependencies as needed.

## Running the MCP Server

The MCP server is implemented in `main.py`.

### Run with FastMCP Inspector

The FastMCP Inspector provides a UI for testing and debugging the MCP server and its tools.

```bash
uv run fastmcp dev inspector main.py
```

This allows you to interactively inspect the available MCP tools and test requests.

### Run the MCP Server

To run the MCP server directly:

```bash
uv run fastmcp run main.py
```

## Claude Desktop Integration

FastMCP provides a convenient way to install the MCP server into Claude Desktop.

Run:

```bash
uv run fastmcp install claude-desktop main.py
```

After installation:

1. Open Claude Desktop.
2. Restart Claude Desktop if required.
3. Verify that the **Expense Tracker MCP Server** is available.
4. You can now interact with the expense tracker using natural language.

For example:

```text
Add an expense of ₹500 for groceries.
```

or:

```text
What did I spend on food this month?
```

## Project Structure

```text
expense-tracker-mcp-server/
│
├── main.py              # MCP server entry point
├── pyproject.toml       # Project configuration and dependencies
├── uv.lock              # Locked dependencies
├── .venv/               # Virtual environment
└── README.md            # Project documentation
```

## Development Workflow

A typical development workflow is:

```text
Create / Update MCP Tool
        │
        ▼
Run FastMCP Inspector
        │
        ▼
Test MCP Tools
        │
        ▼
Run MCP Server
        │
        ▼
Install in Claude Desktop
        │
        ▼
Test using Natural Language
```

## Useful Commands

| Purpose                    | Command                                         |
| -------------------------- | ----------------------------------------------- |
| Initialize project         | `uv init`                                       |
| Create virtual environment | `uv venv .`                                     |
| Install Node.js            | `brew install node`                             |
| Run FastMCP Inspector      | `uv run fastmcp dev inspector main.py`          |
| Run MCP server             | `uv run fastmcp run main.py`                    |
| Install in Claude Desktop  | `uv run fastmcp install claude-desktop main.py` |

## Troubleshooting

### FastMCP command not found

Use `uv run` so that the command runs in the project's managed environment:

```bash
uv run fastmcp run main.py
```

### Claude Desktop does not show the server

Try reinstalling the MCP server:

```bash
uv run fastmcp install claude-desktop main.py
```

Then restart Claude Desktop.

### Inspector is not working

Make sure Node.js is installed:

```bash
node --version
```

If it is not installed:

```bash
brew install node
```

Then run:

```bash
uv run fastmcp dev inspector main.py
```

## License

Add your project's license information here.
