---
tags:
  - security
  - web
---
A tool to intercept requests in [[Burp Suite]].
# Intercept Traffic
1. `Intercept On`
2. `Open Browser`
3. Go to whatever website
# Setup With FoxyProxy
1. Install foxy proxy
2. Setup with proxy configuration:
![[Burp Suite Proxy-1791691713776.webp]]
3. Change burp proxy setting
![[Burp Suite Proxy-1791691688991.webp]]
4. Go to 127.0.0.1:8081 and download the certificate
5. Add the cert to CA authorities list.