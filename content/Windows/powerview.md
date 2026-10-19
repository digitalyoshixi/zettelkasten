---
tags:
  - windows
---
A [[Lightweight Directory Access Protocol|LDAP]] tool to gather the tree of the environment.
# Installation
Python version `3.12.4`
```
git clone https://github.com/aniqfakhrul/powerview.py
cd powerview.py
python -m venv venv
source venv/bin/activate
pip install .
```
# Ldap Filters
```
Get-DomainGroup -LDAPFilter "(objectSid=S-1-5-21-539254891-1587228472-219755335-519)"
```
- Gets whichever entry has objectSID set to that
# Connecting to LDAP Queries
```
powerview $USER:$PASSWORD@$DC
```
# Connectign With WebUI
```
powerview $USER:$PASSWORD@$DC --web
```
Default port 5000
# LDAP
### Get All Computers
```
Get-DomainComputer
```
### Get All Users
```
Get-DomainUser
```
### Get User Properties
```
Get-DomainUser <username> -Properties dnshostname
```
### Get Groups User is a part of
```
Get-DomainGroup MemberIdentity <username>
```
### Getting All Computers User has Local Admin Access to
```
Find-LocalAdminAccess
```
### Getting All [[Group Policy Object|GPO]]
```
GetDomainGPO -Properties displayName,distinguishedName
```
# DNS
### VIew DNS Zones
```
Get-DomainDNSZone
```
### Add DNS Record
```
Add-DomainDNSRecord -ZoneName "local.catbird.net" -RecordName "danielrecord" -RecordAddress "10.0.0.55"
```
### Get DNS Record
```
Get-DomainDNSRecord -ZoneName "local.catbird.net" -Identity "danielrecord"
```
# [[Active Directory Certificate Services|ADCS]]
### Getting Certificate Servers
```
Get-DomainCA
```
### Getting Certificate Template
```
Get-DomainCATemplate -Identity 'SubCA'
```
