---
tags:
  - programming
  - math
---
# Question
Define $L_{3} = \{ x \in \Sigma^{*}  | (\text{ x has palindromic substring of length 3 or more} \vee (|x| = 4))\}$
# Python Verifier
```python
import lang
import utils
import reg

class L(lang.BaseLanguage):
	def has(self,x):
		l = len(x)
		if l == 4: return 1
		for i in range(l):
			for j in range(i+3,l+1):
				s = x[i:j]
				if (s == s[::-1]): return 1
		return 0

l = L()
r = reg.RegexLanguage("(0+1)(0+1)(0+1)(0+1) + (0+1)* (000 + 010 + 101 + 111 + 0000 + 1111 + 0110 + 1001) (0+1)*")
lang.comp(l, r)
```