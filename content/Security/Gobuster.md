---
tags:
  - web
  - redteam
---
Gobuster is noisy and will be noticed. It is a brute forcing tools used mainly to find directories
Similar tool is [[Wfuzz]]
# Aliasing
```
alias gobusterz='gobuster dir -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt -u $1'
```
# Directory Scan
```
gobuster dir -u <target> -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt
```
# File Scan
```
gobuster dir -u <target> -w /usr/share/seclists/Discovery/Web-Content/common.txt -x php,aspx,jsp,old,bak,xml,json,txt,sql,conf,config
```
### Virtual Host Scan
```
gobuster vhost -u URL -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt --append-domain
```
# Flags
- -x for file extension types. Eg: -x php
- -t for thread count. Eg: -t 40