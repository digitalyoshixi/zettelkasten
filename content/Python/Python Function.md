---
tags:
  - python
---
Requires:
- A name
- Arguments
- Actions
- Return type (optional)
# Optional Arguments
`somefunction([, optionalargument])`
Square brackets mean this argument is optional. You don't need to provide it.
Square brackets are nested, if you have multiple optional arguments
`somefunction(arg1, [, arg2 [,arg3]])`
Alternatively:
`somefunction(optionalargument = None)`
# Positional Arguments
`func(a,b, /, c, d)`
The `/` specifies that `a` and `b` are positional arguments.


