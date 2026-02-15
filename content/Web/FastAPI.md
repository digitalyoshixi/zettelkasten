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

items = []
app = FastAPI()

@app.get("/", status_code=200)
def root():
	return {"Hello" : "World"}

@app.post("/items", status_code=201)
def create_item(item : str):
	items.append(item)
	return items
	
@app.get("/items/{item_id}", status_code=200)
def get_item(item_id : int) -> str:
	item = items[item_id]
	return item
```
To run, do `uvicorn <file>:app --reload`
![[FastAPI-20250203012610611.webp]]