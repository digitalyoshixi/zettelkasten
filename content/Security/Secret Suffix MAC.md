---
tags:
  - security
  - cryptography
---
A method of implementing [[Message Authentication Code|MAC]] with 
$$\text{MAC}(\text{message}, \text{key}) = \text{Hash}(\text{message}||\text{key})$$
# Formal Definition
$m = h(x||k) = h(x_{1}||\dots||x_{n}||k)$
- In case of message $x$ being larger than blocksize (like 512 for [[Secure Hashing Algorithm|SHA]])
# Vulnerabilities
- [[Secret Suffix Forgery Attack]]