---
tags:
  - IT
  - networking
aliases:
  - Web Cache
---
A [[Server]] used as a [[Server Cache]] for other servers.
![[Cache Server-20251105160037324.webp|214]]
# Response Headers
- `X-Cache: hit` : Served from Cache
- `X-Cache: miss` : No cache, this key is saved
- `X-Cache: dynamic` : No cache, response is dynamically generated
- `X-Cache: refresh`: Cached content was outdated, refreshed
# Types
- [[Redis]]
- [[MemCached]]
# Methods
- [[Write Around Cache]]
- [[Write Through Cache]]