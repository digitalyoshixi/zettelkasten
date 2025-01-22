---
tags:
  - malware
  - PE
---
### Hint/Name table

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfg_tmp_4e6f187abe6fb46b.png)

- `Hint`**:** A word that contains a number, this number is used to look-up the function, that number is first used as an index into the export name pointer table, if that initial check fails a binary search is performed on the DLL’s export name pointer table.
    

- `Name`**:** A null-terminated string that contains the name of the function to import.
    