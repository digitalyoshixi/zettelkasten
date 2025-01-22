---
tags:
  - javascript
  - bash
  - linux
---
Turning bash commands into trees.
# Nodes
### Node Values
### Node Types
This is `(string)ast[prop]`
##### Script
Commands that form the body of the script
##### Command
Built in or external commands to execute
##### Pipeline
Commands that are concatenated with pipes(|)
##### Logical Expression
2 commands concatenated with a (&&) or (||) operator
##### Function
Represents a defined function
##### Name
Represents the name of a function or variable
##### Compound List
Represents group of commands within for, while, if, else, case, etc nodes
##### Subshell
1 or more commands executed in a seperate shell environment
##### For
Denoting beginning of for statement
##### Case
Denoting beginning of case statement
##### Redirect
Represents input or output stream of command from a stream to another stream