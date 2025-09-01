---
tags:
  - linux
---
A linux command to change the file attributes of a file.
Its like chmod but instead of file permissions it is file attributes.

`chattr +i filename` will make the file immutable
`chatter -i filename` will make file writable again

Useful for adding a `king.txt` in [[Attack Defense CTF|AD CTF]]