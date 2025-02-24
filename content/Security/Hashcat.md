---
tags:
  - security
---
# Hashcat for `/etc/shadow`
```
sudo hashcat --show -m 1800 shadow.txt
```
# Hashcat for `zip`
1. `zip2john ./file.zip > ziphash.txt`
2. `sudo hashcat -a 0 -m 13600 ziphash.txt`