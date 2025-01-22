---
tags:
  - windows
---
1. Get the ISO made from the tool:https://www.microsoft.com/en-ca/software-download/windows10 and etch it with [[BalenaEtcher]]
2. When it asks for account creation, use test@test.com and enter a random password to skip microsoft account creation
3. Settings > Ease of access > advanced > disable animations
4. Microsoft activation scripts https://github.com/massgravel/Microsoft-Activation-Scripts/tree/master
5. Microsoft debloat https://github.com/Sycnex/Windows10Debloater
### Partitioning
![[Windows-20240704033846227.webp|417]]
Windows will automatically make a EFI Systerm Reserved partition, the primary C:/ partition and a recovery partition.