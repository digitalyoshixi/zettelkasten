---
tags:
  - web
  - security
aliases:
  - Cache Deception
---
Tricking a [[Cache Server]] into storing sensitive user data so that attackers can access it later.
# Types
- [[Path Mapping Cache Deception]]
- [[Delimiter Cache Deception]]
- [[Decoding Cache Deception]]
- [[Static Directory Cache Deception]]
- [[Normalization Cache Deception]]
- [[File Name Cache Deception]]
# Tools
- [[Param Miner]]
- [[Web Cache Deception Scanner]]
# Protection
- Always use `Cache-Control` to mark dynamic resources with `no-store` and `private`
- Configure [[Content Delivery Network|CDN]] so that caching doesn't overwrite `Cache-Control`
- Activate protection your CDN has against web cache deception
- Verify there aren't discrepancies between how origin and cache interpret URL paths