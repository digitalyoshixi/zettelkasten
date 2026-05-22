---
tags:
  - security
  - web
aliases:
  - Web Vulnerabilities
---
# Vulnerabilities
- [[SQL Injection|SQLI]]
- [[Cross Site Scripting|XSS]]
- [[Server Side Template Injection]]
- [[Cross Site Request Forgery|CSRF]]
- [[Path Traversal]]
- [[Server Side Request Forgery]]
- [[IFrame Injection Attack]]
- [[XML External Entity]]
- [[Cookie Sandwich]]
- [[Cache Poisoning]]
- [[Web Cache Deception]]
- [[Evil Regex]]
- [[Chained Cross Site Request Forgery Attack]]
- [[Type Confusion]]
- [[Insecure Direct Object Reference|IDOR]]
- [[MIME Sniffing]]
- [[Prototype Pollution]]
- [[HTML Injection]]
- [[Subdomain Takeover]]
- [[Session Puzzling]]
- [[HTTP Verb Tampering]]
- [[HTTP Parameter Pollution]]
- [[HTTP Splitting]]
- [[LDAP Injection]]
- [[NoSQL Injection]]
- [[Server Side Include Injection]]
- [[XPath Injection]]
- [[IMAP Injection]]
- [[Command Injection]]
- [[CSS Injection]]
- [[Cross Site Flashing]]
- [[Clickjacking]]
- [[JSONP Origin Policy Bypass]]
- [[Race Condition]]
- [[Business Logic Vulnerability]]
- [[Mass Assignment Vulnerability]]
- [[Host Header Injection Vulnerability]]
### Subdomains
- [[GraphQL Security]]
# Concepts
- [[Same Origin Policy]]
- [[Basic Authentication]]
- [[Session Token]]
- [[JSON Web Token|JWT Token]]
- [[Open Auth|OAuth]]
- [[OWASP Top 10]]
- [[Out-of-Bound Application Security Testing]]
- [[Content Security Policy|CSP]]
- [[Cross Origin Resource Sharing|CORS]]
- [[Web Server Fingerprinting]]
- [[Rich Internet Application Cross Domain Policy]]
- [[Session Management Schema]]
- [[Common Gateway Interface]]
- [[Server Side Include]]
# Enumeration
### [[Open Source Intelligence|OSINT]]
- [[Google Dorking]]
- [[Github OSINT]]
- [[Swagger]]
- https://securitytrails.com
- https://crt.sh/
### Passive Enumeration
- [[Wappalyzer]]
- Unminify [[JavaScript]] and use regex to search for:
	- API endpoints
	- Secrets
	- API keys
	- Comments
	- Dev shortcuts
	- Application logic
### Active Enumeration
- [[Gobuster]]
- [[Nmap]]
- [[Tinyproxy]]
- [[IIS Private IP Disclosure]]
- [[IIS Tilde Enumeration]]
# Methodology
1. Unauthenticated accessible findings
2. Config/session managment vulns
3. Authorization vulns
4. External API issues
5. Business logic issues