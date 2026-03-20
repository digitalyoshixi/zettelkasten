---
tags:
  - file
aliases:
  - .zip
---
A [[Archive File Format]] that support [[Lossless Compression]].
- [[Multipurpose Internet Mail Extensions|MIME]] `application/zip`
# Format
![[Zip File-20260320225342652.webp]]
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
### Data Descriptor
An optional section added when a zip file is encrypted.
Contains information for decryption.
![[Zip File-20260313164905021.webp]]
- Magic Number
- [[Cyclic Redundancy Check|CRC]]
- Compressed size
### Central Directory (DIR Entry)
Comprised of directory entries (can be thought of as the expanded form of the local header in records)
![[Zip File-20260313144827455.webp]]
### End of Central Directory Record
- Located at the end.
- Can be moved to add new files to the zip archive
- Can be modified to hide a file from being unzipped
![[Zip File-20260313143452737.webp]]
Contains:
- Number of dir entries in central directory
- Offset of the first directory entry
- Size and offset of itself
- Comments