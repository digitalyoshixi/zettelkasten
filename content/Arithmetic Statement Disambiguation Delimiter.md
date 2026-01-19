---
tags:
  - programming
---
A method to disambiguate
# Example
With grammar:
```
<expn> -->  <expn> + <expn> | 
			<expn> - <expn> |
			<expn> * <expn> |
			<expn> / <expn> |
			<expn> ^ <expn> |
			(<expn>)  |
			<identifier> |
			<literal>
```
Example of ambiguous statement is: $8-3*2$
![[Arithmetic Statement Disambiguation Delimiter-20260119213813778.webp]]
We disambiguate with precedence.
```
<expn> -->  <expn> <add-op> <expn> | <mult-ex
```