---
tags:
  - security
  - IT
---
A [[Security Assertion Markup Language|SAML]] implementation used for [[Single Sign On|SSO]] into a network.
It is [[Federated]] and [[Open Source Software|OSS]]
Consists of:
- [[SAML Identity Provider|IdP]]
- [[SAML Service Provider|SP]]
# Installation
1. Ensure you are using a [[Redhat Package Manager|RPM]]-based package manager like [[yum]]
2. Copy the raw file https://shibboleth.net/downloads/service-provider/RPMS/ for amazonlinux2023 into `/etc/yum.repos.d/shibboleth.repo` 
3. `sudo yum makecache`
4. `sudo yum install shibboleth.x86_64`
5. All config files will be in `/etc/shibboleth`
# Protocol
![[Drawing 2025-05-24 22.40.28.excalidraw]]
- All [[Security Assertion Markup Language|SAML]] messages are digitally signed to be encrypted