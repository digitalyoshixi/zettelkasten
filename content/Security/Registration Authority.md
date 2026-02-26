---
tags:
  - security
---
An intermediary between the [[Certificate Authority|CA]] and [[Public Key Infrastructure|PKI]] system.
Used to:
- Verify and approve identities during [[Certificate Signing Request|CSR]]
- Revoke certificate and add to [[Certificate Revocation List|CRL]]
- Pass on requests for the [[Certificate Authority|CA]] to sign
Often setup when direct communication with [[Certificate Authority|CA]] is impractical.