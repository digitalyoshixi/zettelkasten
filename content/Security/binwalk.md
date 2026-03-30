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
# Entropy
```
binwalk -E ./myfile
```
Can be used to create an entropy graph.
- Low entropy -> predictable data, perhaps plaintext
- High entropy -> binary file format
![[binwalk-20260320233839862.webp]]