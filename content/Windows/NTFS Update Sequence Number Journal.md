---
tags:
  - forensics
  - windows
  - file_system
aliases:
  - $UsnJrnl
---
Provides monitoring of file and folder changes, but doesnt hold data.
Contains two streams using [[Alternate Data Stream|ADS]].
Located at `$Extend\$USNJrnl`
- `$J` holds records of changes (creations, modification, deletions, renamings, modifications, etc) over file lifecycle