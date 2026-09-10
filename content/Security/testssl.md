---
tags:
  - security
---
A tool to check supported cryptographic algorithms a [[Digital Certificate|Certificate]] allows for for a website.
Alternatively, use [[sslscan]]
# Usage
```
testssl https://mysite.com
```
### Scan From File
```
testssl --file scope_ips.txt --jsonfile test_ssl_out.json
```
Grep for:
- `(self signed)`
- `expired`
- `TLS 1`
- `Grade capped to M`
- `Grade capped to T`