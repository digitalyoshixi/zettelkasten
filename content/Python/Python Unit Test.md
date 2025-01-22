---
tags:
  - python
---
sumfunc.py:
```python
from typing import List
def getsum(nums : List[int]) -> int:
	sum =0
	for i nums:
		sum+=i
	return sum
```
testsum.py:
```python
import unittest

class TestSum(unittest.TestCase):

	def test_sum_examples_1(self):
		self.assertEqual(getsum([1,2]), 3)

	def test_sum_examples_2(self):
		self.assertEqual(getsum([1,2,3,4]), 10)

if __name__ == '__main__':
	unittest.main(exit=False)
```
Each method must start with the words `test`
# Python Test Types
### Size
Size is the length of the argument
For:
- String
- Int
### Dichotomy
If the argument evaluated as a boolean like, it can be true or false, it can be even or odd, etc. Test with the opposite version
- Boolean
### Boundaries
Giving arguments that hit specific function logic condition branches
- String
- Int
### Order
Giving arguments with same length but the content is rearranged
- String
- Int
# Specific Datatypes
### String
- Punctuation
- Length
- Symbols