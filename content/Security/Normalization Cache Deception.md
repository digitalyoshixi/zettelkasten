---
tags:
  - web
  - security
---
A [[Web Cache Deception|Cache Deception]] attack that involves cache server and origin server [[Path Normalization]] being different
# Example
```
/static/..%2fprofile
```
- Cache server sees it as `/static/..%2fprofile`
- Origin server sees it as `/profile`
# Identification
- Always use `%2f` as the second `/`
- Try permutations of `%2e`, `%2f` to check encodings
- Check for [[Path Normalization]] in Origin server
	- Start with `/static`, path traverse to `/target_endpoint`
- Check for [[Path Normalization]] in Cache server
	- Start with `/target_endpoint`, path traverse to `/static`
