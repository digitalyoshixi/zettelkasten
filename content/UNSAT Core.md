---
tags:
  - verification
  - programming
---
The minimal subset of assertions that makes a statement unsatisfiable.
# Example
With 5 assertions:
- A1: x > 0
- A2: y > 0
- A3: x + y < 1
- A4: z = 42
- A5: w = "hello"
 we can optimize to say the statement is unsatisfiable with just 3 statements:
 - A1
 - A2
 - A3