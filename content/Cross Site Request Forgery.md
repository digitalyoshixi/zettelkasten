---
tags:
  - web
  - security
aliases:
  - CSRF
---
A web exploitation technique that targets a browser session of an authenticated user by having them send a [[Rest API|HTTP Request]] of similar structure to the website they are authenticated on to allow an attacker to benefit.
# Example
If a vulnerable website has the following API structure:
`http://securibank.com/transfer.do?acct=[RECEPIENT]&amount=[DOLLARS]`

If an attacker knows this, they can allow the user to send this request.
- Getting the user to click on a button to send a POST request
- Ensuring some html content is loaded with GET request (`<img src="http://securibank.com/transfer.do?acct=[RECEPIENT]&amount=[DOLLARS]" width="0" height="0" border="0">`)
# Solutions
- [[Referrer Header]]
- [[One Time Form Code]]
