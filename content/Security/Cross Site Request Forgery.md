---
tags:
  - web
  - security
aliases:
  - CSRF
  - XSRF
---
A web exploitation that targets an authenticated user on one website.
A fraud website forces the user to send a request to a protected endpoint on the authenticated site, possibly allowing deleting of account or sending of money to attacker.
![[Cross Site Request Forgery-20251121185141300.webp]]
# Example
If a vulnerable website has the following API structure:
`http://securibank.com/transfer.do?acct=[RECEPIENT]&amount=[DOLLARS]`
If an attacker knows this, they can allow the user to send this request.
- Getting the user to click on a button to send a POST request
- Ensuring some html content is loaded with GET request (`<img src="http://securibank.com/transfer.do?acct=[RECEPIENT]&amount=[DOLLARS]" width="0" height="0" border="0">`)
# Solutions
- [[Referrer Header]]
- [[One Time Form Code]]
