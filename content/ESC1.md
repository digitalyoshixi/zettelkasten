---
tags:
  - windows
  - security
aliases:
  - Enrollee Supplied Subject for Client Authentication
---
An attack against [[Active Directory Certificate Services]].

Exploits certificate templates and allows attackers to specify arbitrary [[Subject Alternative Name Certificate]] from certificate templates.
# Requirements
- Not requiring management approval
- Local user must be able to enroll new certificates with the caused by the `CT_FLAG_ENROLEE_SUPPLIES_SUBJECT` being enabled
- The certs have [[Extended Key Usage]] settings that allow for authentication such as:
	- Client Auth (OID 1.3.6.1.5.5.7.3.2)
	- PKINT Client Auth (1.3.6.1.5.2.4)
	- Smart Card Logon (OID 1.3.6.1.4.1.311.20.2.2)
	- Any Purpose (OID 2.5.29.37.0)
	- No EKU (SubCA)
- Local user must be able to specify [[Subject Alternative Name Certificate|SAN]] in the [[Certificate Signing Request|CSR]]
- The certificate must be enabled
# Finding with [[certipy]]
Use the [[certipy]] `find` command:
- Look for `Enrollee supliessubject and template allows client authentication`
- Look for `Enrollee Supplies Subject : True` in the output
- Look for `Client Authentication : True`
- Look for `User Enrollable Principals` showing a group accessible to many users like `CORP.LOCAL\Domain Users`
- Look for `Requires Manager Approval : False`
- Look for `Authorized Signatures Required : 0`