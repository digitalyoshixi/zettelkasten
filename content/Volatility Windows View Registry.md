---
tags:
  - forensics
  - security
---
# Viewing User Registry
```
python3 vol.py -f <FILE> windows.registry.userassist
```
- Can show # of times program was launched by the user
- Can show # of times process was focused by the user
# Viewing Hive List
```
python3 vol.py -f <FILE> windows.registry.hivelist
```
### Filtering Hive List
```
python3 vol.py -f <FILE> windows.registry.hivelist --filter Doe\\ntuser.dat
```
### Dumping Filtered Hive
```
python3 vol.py -o ./output_folder -f <FILE> windows.registry.hivelist --filter Doe\\ntuser.dat --dump
```
# Viewing Key
```
python3 vol.py -f <FILE> windows.registry.printkey --key "Software\Microsoft\Windows\CurrentVersion"
```
### Viewing Key and Subkeys
```
python3 vol.py -f <FILE> windows.registry.printkey --key "Software\Microsoft\Windows\CurrentVersion" --recursve
```