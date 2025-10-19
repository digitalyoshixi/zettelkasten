---
tags:
  - programming
  - python
---

```python
import importlib, sys
# code = marshal.loads(b'')
code = compile("print('hello')", "example.py", "exec")
pyc_data = importlib._bootstrap_external._code_to_timestamp_pyc(code)
print(pyc_data)
with open('file.pyc', 'wb') as f:
    f.write(pyc_data)
```