---
tags:
  - jail
aliases:
  - Python Jail
---
A restricted python environment that limits what users can do inside a python interpreter.
- Execution is through [[Serial Communication]] to prevent vulerabilities
- Has sanitation of user input
It is NOT a [[Sandbox]]. A sandbox has an independent environment.
![[Pyjail-20240912173826252.webp]]

Commonly created by:
- disabling build-in functions like ( open(), exec(), eval(), etc )
- Limiting imports
- Overriding the [[Python __builtins__]] dictionary
# Escape Techniques
- [[Pyjail Built-ins Exploitation]]
- [[Pyjail FIle Reading Techniques]]
- [[Python lower()]]
- [[Python exec()]]
- [[Python os]]
- [[Python Import]]
- [[Python Object]]
- [[Python Bytecode]]
- [[pip]]
- [[Python breakpoint()]]
# Process
https://github.com/salvatore-abello/python-ctf-cheatsheet/blob/main/pyjails/how-to-solve-a-pyjail.md
1. [[Pyjail Recon]]
2. [[Pyjail Built-ins Exploitation]]

# Resources
- https://github.com/salvatore-abello/python-ctf-cheatsheet/blob/main/pyjails/how-to-solve-a-pyjail.md
- https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes