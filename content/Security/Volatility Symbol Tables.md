---
tags:
  - forensics
  - memory
aliases:
  - Intermediate Symbol File
  - ISF
---
The rules used to reconstruct kernel data from raw memory dumps.
Includes:
- Offset of where structure is
- template/layout of structure definition (fields, sizes, types)
Comes in ISF of [[JSON]] format
- Windows symbols are easy as linux publishes [[Program Database File|PDB]]
- Linux symbols vary by distro, version, architecture and config
# Remote Symbol Tables
```
python3 vol.py --remote-isf-url 'https://github.com/Abyss-W4tcher/volatility3-symbols/raw/master/banners/banners.json' -f <memory_dump> <plugin>
```
# Creating Custom Symbols
- https://volatility3.readthedocs.io/en/latest/getting-started-linux-tutorial.html#procedure-to-create-symbol-tables-for-linux