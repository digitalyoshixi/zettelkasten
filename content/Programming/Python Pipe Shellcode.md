---
tags:
  - programming
  - python
---
# Example
```
python3 -c "import sys; sys.stdout.buffer.write(b'a' * 28 + b'\x99\x99\x99\x99')" | ./binary
```
# [[Pwndbg]] Pipe
```
run < <(python -c "import sys; sys.stdout.buffer.write(b'a' * 25 + b'\x99\x99\x99')")

```
