---
tags:
  - security
  - web
---
An attack that involves exploiting web servers that take user parameters and send them as commands on the server's operating system.
- You can chain another command with `&`

```python
def ping():
    host = request.args.get("host", "127.0.0.1")
    output = os.popen(f"ping -c 1 {host}").read()
    return f"<pre>{output}</pre>"
```
# Chaining Commands
- `;` run another command after
- `&` run another command after
- `&&` run another command if first command works
- `||` run another command if first command fails
- `$(cmd)` [[Subshell]]
- `?` acts as a wildcard for a single character
# Useful Commands
### Linux
- `whoami`
- `uname -a`
- `ifconfig`
- `netstat -an`
- `ps -ef`
### Windows
- `whoami`
- `ver`
- `ipconfig /all`
- `netstat -an`
- `tasklist`
# Writeups
- https://ctftime.org/writeup/40900