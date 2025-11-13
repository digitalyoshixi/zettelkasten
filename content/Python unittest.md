---
tags:
  - programming
  - python
---
A [[Unit Testing]] framework for python.
Uses asserts.
# Boilerplate
```python
import unittest

class myClass():
    def __init__(self,x : int, y : int):
        self.x = x;
        self.y = y;

    def add(self) -> int:
        return self.x + self.y

class myTester(unittest.TestCase):
    def test_add_1(self):
        myclass = myClass(20,30)
        assert(myclass.add() == 50)

if __name__ == "__main__":
	unittest.main()
```
