---
tags:
  - programming
  - pascal
---
A [[Imperative Programming]] language that is really small.
Used commonly to write pseudocode.
# Concepts
- [[Free Pascal Compiler]]
- [[Pascal Variable]]
- [[Pascal Loop]]
- [[Pascal Conditional Statements]]
- [[Pascal Array]]
- [[Pascal 2D Array]]
- [[Pascal Slice]]
- [[Pascal String]]
# [[Free Pascal Compiler|FPC]] Command
```
fpc myfile.pas
```
# Boilerplate
```pascal
program {name of the program}
uses {comma delimited names of libraries you use}
const {global constant declaration block}
var {global variable declaration block}

function {function declarations, if any}
{ local variables }
begin
...
end;

procedure { procedure declarations, if any}
{ local variables }
begin
...
end;
```