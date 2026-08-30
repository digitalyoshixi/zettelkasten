---
tags:
  - security
aliases:
  - Certificate
  - X509 Certificate
  - X.509 Certificate
---
A document used to link a [[Public Key]] to an entity.

Certificates are stored on the local device with [[File Extension]] `.cer` or `.pem`
# Format
- `Version`: x509 version
- `Subject`: DN of subject
- `Subject public key`: Subject's public key
- `Issuer`: DN of its issuer ([[Certificate Authority|CA]] for [[TLS Certificate]])
- `Issuer Digital signature` : Issuer's [[Digital Signature]]
- `Signature algorithm`: Algorithm used to sign cert, includes key size as well
- `CRL endpoints`: List of [[Certificate Revocation List|CRL]] endpoints
- `Authority Information Access (AIA)`: List of issuer CA endpoints
- `CA Constraints`: Constraints on certificate if this certificate can be used for signing other certs
- `Key Usage`: Determines what private key is allowed to do
- `Extended Key Usage`: [[Extended Key Usage|EKUs]]
- `Subject Key ID`: ID for subject, used for hashes in certificate chains
- `Issuer Key ID`: ID for issuer, used for hashes in certificate chains
# Types
- [[TLS Certificate]]
- [[Email Certificate]]
- [[Self-Signed Certificate]]
# Concepts
- [[Certificate Authority|CA]]
- [[Subordinate Certificate Authority|SubCA]]
- [[Certificate Revocation List|CRL]]
- [[Online Certificate Status Protocol]]
- [[Certificate Signing Request]]
- [[Certificate Serial Number]]
- [[Subject Alternative Name Certificate]]
# Attacks
- [[ANS1 Attack X509 Certificate]]
- [[Multiple Common Name Attack]]
- [[PKCS10 Tunnel SQL Injection]]