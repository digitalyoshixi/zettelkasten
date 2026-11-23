---
tags:
  - web
  - security
---
A [[Serialization]] process for PHP objects.
# Example
```
$user->name = "carlos";
$user->isLoggedIn = true;
```
Serialized with `serialize()` is:
```
O:4:"User":2:{s:4:"name":s:6:"carlos";s:10:"isLoggedIn":b:1;}
```
- `O:4:"User"` - An object with 4 character class name `User`
- `2` - object has 2 attributes'
- `s:4:"name"` - key of first attribute is 4 character string `"name"`
- `s:6:"carlos"` - value of first attribute is 6-character string `"carlos"`
- `s:10:"isLoggedIn"` - key of the second attribute is 10-character string `"isLoggedIn"`
- `b:1` - value of the second attribute is boolean `True`