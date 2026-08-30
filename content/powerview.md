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
# Connecting to LDAP Queries
```
powerview $USER:$PASSWORD@$DC
```
# Commands
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