---
tags:
  - web
  - security
---
A [[Web Cache Deception|Cache Deception]] trick that involves:
- Cache server not parsing encoded characters
- Cache server decoding them, and sending them to the origin server
- Origin server that does parse them
# Example
```
/profile%23wcd.css
```
- Cache server sees as regular css
- Origin server sees `/profile#wcd.css`, takes as an parameter