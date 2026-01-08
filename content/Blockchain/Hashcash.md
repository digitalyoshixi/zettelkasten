---
tags:
  - blockchain
  - cryptography
aliases:
  - Hash Cash
---
A [[Proof of Work]] algorithm.
Requires clients concatenate a [[Salting|Salt]] to string and continuously hash until a hash beginning with a certain number of zeroes is found.
# Hashcash Format
### Header
```
X-Hashcash: ver:bits:date:resource.ext::rand:counter
```
- `ver` : Hashcash version
- `bits`: Number of partial pre-image zero bits in the hashed code
- `date`: Time the message was send in format `YYMMDD[hhmm[ss]]`
- `resource`: IP address of email string
- `ext`: Extension - optional
- `rand`: String of random characters encoded in [[Base64]]
- `counter`: Binary counter encoded in base-64
# Algorithm
### Sender
1. Sender initializes a header and appends counter value initialized at random number
2. Compute [[SHA-1|SHA1]] hash, if the first 20 bits are all zero, then this is acceptable, if not, then increment the counter and try to hash again
### Recipient
1. Recipient calculates [[SHA-1]] hash of the message (e.g ``1:20:060408:adam@cypherspace.org::1QTjaYd7niiQA/sc:ePa`)
2. If the first 20-bits arent zero, then the hash is invalid
3. if date is not within two days, its invalid
4. If the email address is not registered by the recipient, or is on a blacklist, the hash is invalid
5. If the hash is already in a database, then that indicates hash re-use, it is invalid