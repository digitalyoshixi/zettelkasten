---
tags:
  - security
aliases:
  - John the Ripper
---
A password cracking tool.
Does not have good [[JSON Web Token|JWT Token]] support 
# Installation
`yay -S john`
# Viewing Version
`john | head -3`
# Formats
`john --list=formats`
- [[John SHA512 Format]]
https://pentestmonkey.net/cheat-sheet/john-the-ripper-hash-formats
# General Cracking with Specific Format
1. `vim hash.txt` with the specific format requirements
2. `john --format=<format> --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`