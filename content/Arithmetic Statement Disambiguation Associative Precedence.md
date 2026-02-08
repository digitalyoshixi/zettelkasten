---
tags:
  - programming
---
Allowing for [[Associative|Left Associative]] or [[Associative|Right Associative]] grammars.
- Left associative: put recursive term before non-recursive term
- Right associative: put recursive term after non-recursive term
# Example
Converting a grammar like this into a left associative one
```
<expn> --> <expn> <add-op> <mult-exp> | <mult-exp>
<mult-exp> --> <mult-exp> <mult-op> <pow-exp> | <pow-exp>
<pow-exp> --> <br-exp> ^ <pow-exp> | <br-exp>
<br-exp> --> (<expn>) | <simple>
<simple> --> <identifier> | <literal>
<add-op> --> + | -
<mult-op> --> * | /
```
We put all recursive terms before non-recursive ones
```
<expn> -->  <expn> <add-op> <mult> | 
			<expn> - <expn> |
			<expn> * <expn> |
			<expn> / <expn> |
			<expn> ^ <expn> |
			(<expn>)  |
			<identifier> |
			<literal>
```