---
tags:
  - c
aliases: []
---
Variables that will survive until the end of the program.
They are a middle ground between [[Local Variables]] and [[Global Variables]]

There are a few uses for them:
- Privacy
- Pertinence

# Pertinance
If they are local variables, then their value persists even when their execution leaves their scope.
# Privacy
There can only be one static variable per file. You do not get variable name conflicts. [[Static Name Collision Avoidance]]

# Other Meanings
The static keyword can also take on different meanings
- Internal linkage. There is only one static variable for all classes. This can be used for a counter of the # of objects 