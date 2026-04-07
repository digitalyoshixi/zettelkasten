---
tags:
  - programming
---
A method to disambiguate [[Ambiguous Context Free Grammar]] by adding delimiters around non-terminals before 
# Example
```
<expn> ->   <expn> + <expn> |
			<expn> - <expn> |
			<expn> * <expn> |
			<expn> / <expn> |
			<expn> ^ <expn> |
			(<expn>) |
			<identifier> |
			<literal> |
```
This is ambiguous and can produce `8 - 3 * 2`
We can disambiguate with delimiters
```
<expn> ->   (<expn>) + (<expn>) |
			(<expn>) - (<expn>) |
			(<expn>) * (<expn>) |
			(<expn>) / (<expn>) |
			(<expn>) ^ (<expn>) |
			(<expn>) |
			<identifier> |
			<literal> |
```
Then we can produce `(8) - ((3)*(2))`