---
tags:
  - security
  - web
aliases:
  - NoSQL Type Confusion
---
A attack against [[Object Relational Mapping|ORM]] to handle strings differently to trigger [[Structured Query Language|SQL]] injection. Make javascript handle types differently.
Send a javascript object that the [[Object Relational Mapping|ORM]] treats as a different type to trigger injections
# Prisma Filter Attack
```
{"email" : {"gte":""}}
```
# JSON Injection
```
{"toString" : "admin"}
```
# Email Edge Case
- If [[Simple Mail Transfer Protocol|SMTP]] server is misconfigured, we can send two emails
```
a@x.com.b@y.com
```