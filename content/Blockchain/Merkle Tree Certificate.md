---
tags:
  - security
  - cryptography
---
A [[Digital Certificate|Certificate]] created by [[Merkle Tree]]. Issue a single certificate, describe multiple certificates.
- You can share the same CA signature across multiple connections
- You can use the merkle tree, sign the tree head, break it down into smaller ones, they are all validated by the tree root
Already used in [[Certificate Transparency Logs]]
- Requires an [[Inclusion Proof]] (4/5 hashes)
# Process
1. CA issue certificate by logging them
2. Log signatures distributed to clients
3. Certificates can (if client is up to date) omit the signature sent to the client
# Tradeoffs
- Clients need state to store, they need state to update
- Servers need to have multiple certificates