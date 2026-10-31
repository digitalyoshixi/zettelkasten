---
tags:
  - security
---
A method to break weak regex whitelists by abusing the URL specification to include more details.
# URL Spec Breaking
```
https://expected-host:fakepassword@evil-host
```
```
https://evil-host#expected-host
```
```
https://expected-host.evil-host
```
# [[Percent Encoding|URL Encoding]] or [[Double URL Encoding]]
Can sometime bypass the whitelist checks