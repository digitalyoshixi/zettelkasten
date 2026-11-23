---
tags:
  - web
  - security
aliases:
  - BSCP
---
# Notes
- Use `location` rather than `window.location`
# SQLI
### Returned SQL
- [[SQLI Comments]]
- [[SQLI UNION Attack]]
- [[SQLI Determining Number of Columns]]
- [[SQLI Determining Column Data Type]]
- [[SQLI Concatenation]]
- [[SQLI Determining Database Type]]
- [[SQLI View Tables]]
### Blind SQL
- [[Blind SQLI Conditional Triggering]]
- [[Error Based SQLI]]
- [[Verbose Error SQLI]]
- [[Time Based SQLI]]
- [[OAST Based SQLI]]
### Filter Bypass
- [[XML SQL Filter Bypass]]
- [[Hackvertor]]
# API Testing
- [[Common API Documentation Endpoints]]
- [[JS Link Finder]]
- [[HTTP Verb Tampering]]
- [[Content-Type Tampering]]
- [[API Route Brute Force Discovery]]
- [[Param Miner]]
- [[Burp Content Discovery]]
### Mass Assignment
- [[Mass Assignment Vulnerability]]
- [[HTTP Parameter Pollution]]
- [[HTTP Parameter Pollution Same Parameter Trick]]
- [[HTTP Parameter Pollution via Web Routes]]
- [[HTTP Parameter Pollution via Backend JSON]]
- [[Burp Suite Backslash Powered Scanner]]
# Cache Exploitation
- [[Path Mapping Cache Deception]]
- [[Delimiter Cache Deception]]
- [[Decoding Cache Deception]]
- [[Static Directory Cache Deception]]
- [[Normalization Cache Deception]]
- [[File Name Cache Deception]]
# CSRF
- [[CSRF SameSite Bypass with GET Request]]
- [[CSRF Gadget]]
- [[Cross Site Request Forgery Token Forgery]]
# Username Enumeration
- [[Username Enumeration by Subtle Response Differences]]
- [[Username Enumeration by Response Timing]]
- [[Username Enumeration by Lockout]]
### Brute Forcing
- [[Brute Force X-Forwarded-For Spoofing]]
- [[Brute Force Reset by Valid Account Login]]
- [[Burp Suite Turbo Intruder|Single Packet Attack]]
# Authentication
### Session Tokens
- [[Session Token Predictable Generation]]
### 2FA
- [[2FA Bypass by Forced Browsing]]
- [[2FA Bypass by Verification Code Brute Force]]
### Remember Me 
- [[Remember Me Token Forgery]]
### Password Reset
- [[Password Reset Insecure Token Validation]]
- [[Password Reset Token X-Forwarded-Host Phishing]]
### Password Change
- [[Password Brute Force via Password Change]]
# Clickjacking
- [[Clickjacking]]
- [[Clickbandit]]
# Web LLM Attacks
- [[Indirect Prompt Injection]]
- [[Prompt Injection]]
- [[Training Data Leakage Prompt Injection]]
- [[AI Scanner Agent Prompt Injection]]
- [[Data Exfiltration by AI Scanner Agents]]
- [[SSRF by AI Scanner Agents]]
# Path Traversal (Usually on static files)
- [[Path Traversal]]
- [[Nested Path Traversal]]
- [[Encoding Path Traversal]]
- Burp intruder `Fuzzing - Path Traversal` to check
- [[Null Character File Extension Filter Bypass]]
# File Upload Vulnerabilities
- [[Web Server Static File Handling Logic]]
- [[Webshell]]
- [[Webshell Upload To Non-User Directories by Path Traversal]]
- [[FIle Upload Server Configuration Overwrite]]
- [[File Extension Obfuscation]]
- [[exiftool]]
- [[File Upload Race Condition]]
- [[Default Supported PUT Endpoint Vulnerability]]
# NoSQL Injection
- [[NoSQL Syntax Injection]]
- [[NoSQL Operator Injection]]
- [[MongoDB Injection]]
# OAuth
- [[Open Auth|OAuth]]
- [[OAuth Authentication Bypass via OAuth Implicit Grants]]
- [[OAuth Missing CSRF Protections]]
- [[OAuth redirect_uri Hijacking]]
# Prototype Pollution
- [[JSON]]
- [[Javascript Prototype]]
- [[Prototype Pollution]]
### Client side
- [[Prototype Pollution via URL]]
- [[Prototype Pollution via JSON]]
- [[Prototype Pollution via Constructor]]
- [[Prototype Pollution via Flawed Sanitiziation]]
- [[Prototype Pollution via Fetch()]]
- [[Prototype Pollution via defineProperty()]]
- [[XSS Sink]]
### Server side Identification
- [[Prototype Pollution Property Reflection]]
- [[Prototype Pollution Status Code Overwrite]]
- [[Prototype Pollution JSON Spaces Overwrite]]
- [[Prototype Pollution Charset Overwrite]]
### Server side RCE
- [[Prototype Pollution Child Process Spawning]]
- [[Prototype Pollution Environment Variable Overwriting]]
# GraphQL
- [[GraphQL]]
- [[GraphQL Request Methods]]
- [[GraphQL Query]]
- [[GraphQL Introspection]]
- [[GraphQL Suggestions]]
- [[GraphQL Alias Overloading]]
- [[GraphQL CSRF]]
# JWT
- [[JSON Web Token|JWT Token]]
- [[JWT Editor]]
- [[JWT Bypass via Missing Signature Validation]]
- [[JWT Bypass via none Signature Acceptance]]
- [[JWT Cracking Guide]]
- [[JWT Embedded JWK Attack]]
- [[JWT Owned JKU Domain Attack]]
- [[JWT kid From Path Attack]]
# HTTP Request Smuggling
# XSS
# XXE
- [[XML External Entity|XXE]]
- [[XXE File Retrieval]]
- [[XXE SSRF Attack]]
- [[XXE From XInclude]]
- [[XXE From SVG File Upload]]
- [[XXE Out of Bound Data Exfiltration]]
- [[XXE Error Message Exfiltration]]
# Insecure Deserialization
- [[PHP Serialization]]
- [[Java Serialization]]
- [[Serialized Message Modification]]
- [[PHP Type Conversion Conditional Check Bypass]]