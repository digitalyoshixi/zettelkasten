---
tags:
  - programming
  - linux
---
A command used to change the numbers for command line arguments to a program.
- Argument 3 becomes 2
- Argument 2 becomes 1
- Argument 1 becomes lost
# Example Usage
```bash
category="$1"
shift
/u/sally/"$category"/process "$@"
```