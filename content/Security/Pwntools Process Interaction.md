---
tags:
  - python
  - security
  - binary_exploitation
---
# Immediate Send
```python
import pwn 
pwn.context.log_level = 'debug'
r = pwn.process("./buffer_overflow", aslr=True)
r.send(b"A"*24)
print(r.readall())
```
# Send After Prompt
```python
import pwn 
pwn.context.log_level = 'debug'
r = pwn.process("./buffer_overflow", aslr=True)
r.sendafterline(b'?', b"A"*24)
print(r.recvall().decode())
```