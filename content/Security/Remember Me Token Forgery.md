---
tags:
  - web
  - security
---
Abusing weak Remember me token minting logic to generate your own tokens.
- Allows for access without logging in
- Abuse weak ciphers with no salt
	- [[Message Digest Algorithm 5|MD5]]
	- [[SHA-1|SHA1]]
# Example Formats
```
username:timestamp
username:password
```
# Labs
- https://portswigger.net/web-security/learning-paths/authentication-vulnerabilities/vulnerabilities-in-other-authentication-mechanisms/authentication/other-mechanisms/lab-brute-forcing-a-stay-logged-in-cookie