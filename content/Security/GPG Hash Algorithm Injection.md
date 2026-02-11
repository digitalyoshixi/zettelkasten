---
tags:
  - security
  - cryptography
---
A vulnerability in the implementation of hash signature field in [[GNU Privacy Guard|GPG]] older versions.
You can write any hash version and not-dash escaped + also use [[Carriage Return]] to overwrite data shown to user.
![[GPG Hash Algorithm Injection-20260211033239405.webp]]
![[GPG Hash Algorithm Injection-20260211033558239.webp]]