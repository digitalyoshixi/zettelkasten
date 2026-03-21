---
tags:
  - security
  - cryptography
---
A [[Cryptographic Protocol]] proposed by [[Ronald Rivest]] that achieves confidentiality over insecure channels without need of [[Public-Key Cryptography|Asymmetric Cryptography]].
# Protocol
- Sender uses [[Modified Access Creation|MAC]] to embed genuine data packets with fake 'chaff' packets 
- Reciever 'winnows' by authenticating the [[Modified Access Creation|MAC]] and extracting only the real packets