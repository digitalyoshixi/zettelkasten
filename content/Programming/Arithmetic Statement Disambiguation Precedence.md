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
<expn> -->  <expn> <add-op> <expn> | <mult-exp>
<mult-exp> --> <mult-exp> <mult-op> <mult-exp> | <pow-exp>
<pow-exp> --> <pow-exp> ^ <pow-exp> | <br-exp>
<pow-exp> --> <pow-exp> ^ <pow-exp> | <br-exp>
<br-exp> --> (<expn>)| <simple>
<simple> --> <identifier> | <literal>
<add-op> --> + | -
<mult-op> --> * | /
```
We can remove ambiguity with left or right associativity
```
<expn> --> <expn> <add-op> <mult-exp> | <mult-exp>
<mult-exp> --> <mult-exp> <mult-op> <pow-exp> | <pow-exp>
<pow-exp> --> <br-exp> ^ <pow-exp> | <br-exp>
<br-exp> --> (<expn>) | <simple>
<simple> --> <identifier> | <literal>
<add-op> --> + | -
<mult-op> --> * | /
```
![[Arithmetic Statement Disambiguation Delimiter-20260119214305217.webp]]