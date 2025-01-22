---
tags:
  - web
  - redteam
---
Gobuster is noisy and will be noticed. It is a brute forcing tools used mainly to find directories

Gobuster needs to be installed because it doesn’t come by default. This is a password cracking tool. Once done, on kali linux type this command to make a easy alias of gobusterz:

#### alias gobusterz='gobuster dir -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt -u $1'

  

Then you can run gobusterz if you give it a url.

Some useful flags are:

-x for file extension types. Eg: -x php

-t for threat count. Eg: -t 40

Similar tool is [[Wfuzz]]