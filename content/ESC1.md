---
tags:
  - windows
  - security
---
An attack against [[Active Directory Certificate Services]].

Exploits certificate templates and allows attackers to specify arbitrary [[Subject Alternative Name Certificate]] from certificate templates.
# Requirements
- Not requiring management approval
- Local user must be able to enroll new certificates with [[Extended Key Usage]] that allow for authentication such as:
	- Client Auth (OID 1.3.6.1.5.5.7.3.2)
	- PKINT Client Auth (1.3.6.1.5.2.4)
	- Smart Card Logon (OID 1.3.6.1.4.1.311.20.2.2)
	- Any Purpose (OID 2.5.29.37.0)
	- No EKU (SubCA)
- Local user must be able to specify [[Subject Alternative Name Certificate|SAN]] in the [[Certificate Signing Request|CSR]]
# Tools
- [[certipy]]