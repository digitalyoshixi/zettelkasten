---
tags:
  - security
  - forensics
aliases:
  - Volatility Windows Carve File
---
```
python3 vol.py -f <FILE> -o ./output_directory windows.dumpfile --pid <pid> --virtaddr
```
# Example
1. Get the specific virt address from a search
![[Volatility Windows Dump File-20260323002910408.webp]]
2. Dump command `vol -f ~/Downloads/memimages/20210430-Win10Home-20H2-64bit-memdump.mem -o ./dump windows.dumpfile --virtaddr 0xbf0f6aca1e90`