---
tags:
  - web
  - security
---
Methods to bypass file upload restrictions on file types by obfuscation file names.
# Case Sensitivity
- Try `exploit.pHp` instead of `.php`
# Multiple Extensions
- Try `exploit.php.jpg` and see if it is interpreted as a jpg image
# Ignored Trailing Characters
- Add trailing characters like whitespaces and dots `exploit.php ` `exploit.php.`
# URl Encoding
- Try url encoding characters `exploit%2Ephp`
# Semicolons
- Add semicolons before file extension to abuse lower level functions in C `exploit.asp;.jpg` or `exploit.asp%00.jpg`
# Multibyte unicode
- Try [[Unicode|Multibyte Unicode]] which may be converted into null bytes if UTF-8 parser converts to ascii (single byte). Below might be translated to `x2E` (`.`)
	- `xC0 x2E`
	- `xC4 xAE`
	- `xC0 xAE`
# Simple file extension regex removal
- Abuses systems that just remove regex once, but never again
![[File Extension Obfuscation-20261108201528879.webp]]