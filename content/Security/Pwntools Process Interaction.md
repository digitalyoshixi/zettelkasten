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
pwn.context.arch = 'amd64'
r = pwn.process("./buffer_overflow", aslr=True)
r.sendline(b"A"*24)
print(r.readall())
r.interactive()
```
# Send After Prompt
```python
import pwn 
pwn.context.log_level = 'debug'
r = pwn.process("./buffer_overflow", aslr=True)
r.sendafterline(b'?', b"A"*24)
print(r.recvall().decode())
```
# Remote Connection
```python
import pwn
conn = pwn.remote('ftp.ubuntu.com',21)
```