---
tags:
  - programming
---
Reads source-code and runs the program line-by-line. It runs the program in real-time.
# List of Interpreted Languages
- [[Python]]
# Process
![[Interpreter-20250107003517851.webp]]
1. A [[Tokenizer]] breaks up source code into a stream of tokens
2. A [[Parser]] validates to check if our tokens are syntactically valid
3. Parser converts the tokens into an [[Abstract Syntax Tree|AST]]
4. [[Abstract Syntax Tree|AST]] is interpreted with a [[Recursive Descent Parsing]] or [[Bytecode]]
5. AST is walked bottom-up, and interpreted in a wider envionment
# Types
- [[Bytecode Interpreter]]
- [[AST Interpreter]]
# Creating Interpreted Language
- https://www.youtube.com/watch?v=A3gTw1ZkeK0 
- https://www.youtube.com/playlist?list=PLj_VrUwyDuXRizi2nJjP8uP9Tmh91OLwA
- https://craftinginterpreters.com/contents.html