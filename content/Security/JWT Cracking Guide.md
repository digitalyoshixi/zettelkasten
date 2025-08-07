---
tags:
  - security
---
# Process
1. Create a file `jwt.txt` with the jwt file contents
   ![[JWT Cracking Guide-20250807033850270.webp]]
2. 
```
john jwt.txt --wordlist=/usr/share/wordlists/jwtsecrets.txt --format=HMAC-SHA256  
```

3. 
```
hashcat -m 16500 -a 0 jwt.txt /usr/share/wordlists/rockyou.txt
```
