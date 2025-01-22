---
tags:
  - programming
---
Exceptions are types of errors that occur in stderr which will occur during runtime. You can prevent these exceptions from crashing these programs using [[Java Try Catch Blocks]]

# Common Exceptions
Exception - general exception
Arithmetic Exception - dividing by zero
IOException - Input output error

# Checked Vs Unchecked Exceptions
### Unchecked Exceptions
Occur naturally. these errors are usually not going to happen. 99% of the times these methods are run, errors do not happen.

### Checked Exceptions
You are required to run these methods in a try catch block. If you dont, then the compiler will not let you run it. This is to prevent data corruption.
