---
tags:
  - security
  - cryptography
---
A method of implementing [[Message Authentication Code|MAC]] with 
$$\text{MAC}(\text{message}, \text{key}) = \text{Hash}(\text{key}||\text{message})$$
# Formal Definition
$m = h(k||x) = h(k|||x_{1}||\dots||x_{n})$
- In case of message $x$ being larger than blocksize (like 512 for [[Secure Hashing Algorithm|SHA]])
# Vulnerability
- [[Secret Prefix Length Extension Attack]]