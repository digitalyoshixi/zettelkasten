---
tags:
  - security
  - cryptography
---
An attack against [[Secret Suffix MAC]].
Involves finding a [[Hash Collision]] between the original messages.
$\text{Hash}(\text{M}_{1}) = \text{Hash}(\text{M}_{2}) \implies \text{MAC}_{key}(M_{1})=\text{MAC}_{key}(M_{2})$

https://eitca.org/cybersecurity/eitc-is-acc-advanced-classical-cryptography/message-authentication-codes/mac-message-authentication-codes-and-hmac/examination-review-mac-message-authentication-codes-and-hmac/what-are-the-weaknesses-of-the-secret-prefix-and-secret-suffix-methods-for-constructing-macs/