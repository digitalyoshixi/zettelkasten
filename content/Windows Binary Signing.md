---
tags:
  - windows
  - programming
---
# Self Signed Certificate
- Create with [[OpenSSL]]
```
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365
openssl pkcs12 -inkey key.pem -in cert.pem -export -out sign.pfx
```
- Sign it with `signtool.exe`
```
signtool sign /f sign.pfx /p <pfx-password> /t http://timestamp.digicert.com /fd sha256 binary.exe
```