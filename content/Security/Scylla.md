---
tags:
  - reverse_engineering
  - debugging
---
Scylla is how you dump DLLs.
1. ![[Scylla-20240103010645638.webp]]
2. ![[Scylla-20240103010715244.webp]]
3. All DLLs require an import address table. Let Scylla auto-find that import address table.![[Scylla-20240103010840577.webp]]![[Scylla-20240103010854216.webp]]![[Scylla-20240103010917636.webp]]
4. Now you can save this DLL ![[Scylla-20240103011008845.webp]]

heres how you can run your stolen DLL as an executable:
`rundll32.exe yourdll.dll,DLLMAIN`