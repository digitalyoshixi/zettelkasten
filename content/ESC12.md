---
tags:
  - security
  - windows
aliases:
  - YubiHSM2 Vulnerability
---
A [[Active Directory Certificate Services|ADCS]] [[Privilege Escalation]] attack that uses [[Yubico]]'s [[YubiHSM2]] to sign arbitrary certificate requests.
# Requirements
- CA uses YubiHSM2 for storing and managing its private keys
- Attacker has a low-priv user shell on the system
- Older version of YubiHSM2 vulnerable to this

https://pkiblog.knobloch.info/esc12-shell-access-to-adcs-ca-with-yubihsm