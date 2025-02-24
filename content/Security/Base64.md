---
tags:
  - cryptography
---
A encryption algorithm that takes text and converts it into a ciphered text.
- Often used for sending [[Simple Mail Transfer Protocol|SMTP]] attachments
- 33-37% to original size
- 
# Base64
1. Input is read 6 bits at a time, anything that is not 6-bits is padded with 0s
2. Every 6-bits is mapped to a character in the base64 character range
3. Output is given
# Base64 Character Range
![[Base64-20250223023040044.webp]]
