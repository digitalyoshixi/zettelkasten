---
tags:
  - programming
  - python
---
A type of [[Python Iterator]] that can be produced [[Lazy Evaluation|Lazily]]
Uses [[Python Yield]] keyword.
```python
def generate_range(n : int) -> Generator[int, None, None]:
	yield from range(n)
```