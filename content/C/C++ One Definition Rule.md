---
tags:
  - cpp
aliases:
  - C++ ODR
---
# Files
Inside a file each:
- function
- variable
- type
- template
can only have **one** definition

local variables and scopes **do not violate this rule**
# Programs
Within a program, each:
- function
- variable
can only have **one** definition

make sure you only have one main method retard

However,
- types
- templates
- inline variables
allowed to have duplicate definitions in different files. **only** if the definitions are **identical**
