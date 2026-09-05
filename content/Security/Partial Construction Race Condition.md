---
tags:
  - web
  - security
---
A race condition that occurs to exploit the time window where fields are uninitialzed after object creation.
- User creates account, another request soon after to set API key, abuse this window where API key is null
# Abusing
You must supply user input (URL params, body params, etc) equivalent to this uninitialized value. A few tricks:
### PHP
- `param[]=foo` equivalent to `param=['foo']`
- `param[]=foo&param[]=bar` equivalent to `param=['foo','bar']`
- `param[]` equivalent to `param=[]`
### [[Ruby on Rails]]
- `param[key]` equivalent to `params = {"param"=>{"key"=>nil}}`
- `param[]` would set `param` to nil
