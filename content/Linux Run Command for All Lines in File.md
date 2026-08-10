---
tags:
  - linux
---
```bash
while read -r item; do drill "$item"; dome < scope_domains.txt > output.txt
```