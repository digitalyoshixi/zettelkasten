---
tags:
  - forensics
---
# Display Embedded Data
```
binwalk -e ./file
```
# Extract file
```
binwalk -e ./file
```
# Extract Everything (Unsafe)
```
binwalk -dd " .* " ./file
```