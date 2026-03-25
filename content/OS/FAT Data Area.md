---
tags:
  - file_system
aliases:
---
Comprised of multiple file entries.
The filesystem will stop looking for entries once it runs into `0x00` byte.
![[FAT Data Area-20260314003218610.webp]]
# Directory Entry
![[FAT Data Area-20260314003353299.webp]]
Filename can be:
- [[Short Filename|SFN]]
- [[Long FIlename|LFN]]
# Attribute Flag
Attribute flag is a combination of things
![[FAT Data Area-20260314004459606.webp]]