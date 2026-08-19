---
tags:
  - security
  - web
aliases:
  - CSRF Token
---
These are random tokens used to ensure that the only websites you access can send requests to the website.
Often embedded within forms to automatically add itself to a request.
```
<form name="change-email-form" action="/my-account/change-email" method="POST"> <label>Email</label> <input required type="email" name="email" value="example@normal-website.com"> <input required type="hidden" name="csrf" value="50FaWgdOhi9M9wyna8taR1k3ODOR8d6u"> <button class='button' type='submit'> Update email </button> </form>
```