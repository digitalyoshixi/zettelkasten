---
tags:
  - web
  - python
---
A middleware to create [[Rest API]] or [[GraphQL]]
# Installation
1. `pip install fastapi uvicorn`
# Boilerplate
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
	return {"Hello" : "World"}

items = []
@app.post("/items")
def create_item(item : str):
	items.append(item)
	return items
	
@app.get("/items/{item_id}")
def get_item(item_id : int) -> str:
	item = items[item_id]
	return item
```
To run, do `uvicorn <file>:app --reload`
![[FastAPI-20250203012610611.webp]]