---
tags:
  - programming
  - python
  - machine_learning
---
A usage of [[FastAPI]] for [[Model Context Protocol|MCP Server]].
# Installation
```
pip install "mcp[cli]" httpx
```
# Boilerplate
```python
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("myserver")

async def my_function(myinput : str) -> dict :
	"""
	Get your name with age
	"""
	# logic
	return f"""
	Name: {myinput},
	Age: 20
	"""

if __name__ == "__main__":
	mcp.run(transport="stdio")
```
# Running Test Server
```
mcp dev server.py
```