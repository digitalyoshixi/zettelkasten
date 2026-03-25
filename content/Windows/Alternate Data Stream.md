---
tags:
  - windows
  - forensics
aliases:
  - ADS
---
A feature in [[New Technology File System|NTFS]] that allows a file to have extra streams of data.
# Finding Alternate Data Streams
```
PS F:\> gci -recurse | % { gi $_.FullName -stream * } | where stream -ne ':$Data'
```