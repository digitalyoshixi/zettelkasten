---
tags:
  - programming
---
A [[Top-Down Generation]] [[Parser]]
To create it you must define a:
- [[Operator Precedence]] Table
- [[Backus-Naur Form|BNF]] grammar rule
- 3 Handler functions for parsing tokens. 
	- `AST_EXPR nud(*token)` expects nothing to the left of the token. Used for Unary operations
	- `AST_EXPR led(*token)` expects a token to the left. Used for [[Binary Operation]], [[Postfix Notation]]
- Lookup tables
# Binding Power
This is the degree to which an operator should be preferred. There is a table of operators and their precedence.
![[Pratt Parser-20250129023941736.webp]]
# Blogs
- https://louis.co.nz/2026/03/26/pratt-parsing.html