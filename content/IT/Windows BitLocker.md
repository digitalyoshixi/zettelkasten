---
tags:
  - hardware
aliases:
  - Full Disk Encryption
  - FDE
---
File encryption by microsoft.
Can encrypt **files**, **folders** or an **entire drive** in **real-time**.
Uses user's password as the decryption/encryption key.
Encrypted when the user logs off, decrypted while the user is logged on.
In Windows 11, bitlocker is enabled by default.
Works on [[exFAT]], [[FAT32]], [[FAT16]] and [[New Technology File System|NTFS]].
# File Encryption
![[Windows BitLocker-20240706212417012.webp]]
Right click a file > Properties > Advanced > Encrypt contents to secure data
# Drive Encryption
Requires the motherboard have a [[Trusted Platform Module]].
You can enable bitlocker in [[Windows Control Panel]].
![[Windows BitLocker-20240706213942228.webp]]
# Bitlocker To Go
drive encryption for removable devices. Does not use [[Trusted Platform Module|TPM]] unfortunately.