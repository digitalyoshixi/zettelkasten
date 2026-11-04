---
tags:
  - web
  - security
---
A technique to test [[HTTP Parameter Pollution]] by sending the same parameter with different values.
Certain servers process differently:
- [[PHP]] parses last parameter only
- ASP.NET combines both parameters
- [[NodeJS]] parses first parameter only