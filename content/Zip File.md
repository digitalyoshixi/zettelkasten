---
tags:
  - file
aliases:
  - .zip
---
A [[Archive File Format]] that support [[Lossless Compression]].
- [[Multipurpose Internet Mail Extensions|MIME]] `application/zip`

# Format
### Records
![[Zip File-20260313142336953.webp|400]]
Entries that describe file data compressed with [[DEFLATE]]
- frSignature (PK [[Magic Numbers]])
- frVersion
- Comments
- Compressed file size
- [[Cyclic Redundancy Check|CRC]]
- Uncompressed file size
- Extra fields
	- Exploited to support a ZIP64 format, [[WinZip]] compatibility, [[Advanced Encryption Standard|AES]] encryption, file attributes, [[New Technology File System|NTFS]], [[Unixtime]]
### Central Directory (DIR Entry)
Comprised of directory entries
### End of Central Directory Record
- Located at the end.
- Can be moved to add new files to the zip archive