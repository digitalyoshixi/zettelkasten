---
tags:
  - security
---
This is a vulnerability patching tool for [[Remote Procedure Calls]] discovered by [[ThePrimagen]]
# Vulnerability
RPC calls to netflix endpoints for data that did not exist would create empty objects to return.
If you send a request that had a millions amount of these requested rows, millions of objects would be created, then [[Serialization|Serialized]] back to the user, causing a [[Denial of Service|DoS]] attack to the server.
# Solutions
[[ThePrimagen]]'s solution is to use [[Cloudflare]] [[Denial of Service|DoS]] protection