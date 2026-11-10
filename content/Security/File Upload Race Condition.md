---
tags:
  - web
  - security
---
A vulnerability wherein uploaded temporary files can be executed within the short window that they are being scanned/evaluated.
- Servers must copy the file temporarily into a temp directory to process it
# Attack Methods
- Upload a large file with multiple chunks. Make the malicious payload the start and pad it with bytes
- Sometimes filenames are pseudorandom and can be brute forced