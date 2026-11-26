---
tags:
  - web
  - security
---
A solution to [[Cross Site Request Forgery|CSRF]].
Everytime a request is sent. a randomly generated code is attached to the request.
Anything that the webpage is sent back then must have the same randomly generated code to verify that it came from the same origin.

```html
<form action="/update-profile" method="POST">
  <!-- Hidden CSRF Token Input -->
  <input type="hidden" name="csrf_token" value="a8f5f167f44f4964e6c998dee827110c">
  
  <label for="username">Username:</label>
  <input type="text" id="username" name="username">
  
  <button type="submit">Save</button>
</form>
```