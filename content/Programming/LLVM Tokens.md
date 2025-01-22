---
tags:
  - llvm
---
https://www.youtube.com/watch?v=aYd40eVse7U
These are the words stripped of whitespace and syntax in our programming language. They are the keywords, variables, literals, functions, etc of a language.
# Example
```kaleidoscope
# Compute the x'th fibonacci number.
def fib(x)
  if x < 3 then
    1
  else
    fib(x-1)+fib(x-2)

# This expression will compute the 40th number.
fib(40)
```
Tokens are:
- `#` (comment)
- `def` (tok_def which is a reserved keyword)
- `(` (parenthesis)
- `fib` (tok_identifier)
- `x` (tok_identifier)
- `if` (tok_if which is a reserved keyword)
- `<` (operator)
- `3` (tok_number which is a literal)
- `then` (tok_then which is a reserved keyword)
- `else` (tok_else which is a reserved keyword)
- `x-1` (expression which includes tok_identifier and tok_number)
- `)` (parenthesis)
- ...
# Token Seperators
- ` ` spaces
- `\n` newlines

