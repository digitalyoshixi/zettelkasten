---
tags:
  - malware
  - security
---
# Match at Specific Offset
```
strings:
	$mz = {4d 5a}
conditions:
	// find the magic number at offset 0
	($mz at 0)
```
# Match Anywhere
```
strings:
	$win = "WinHelpW"
conditions:
	$win
```
# Match Multiple Strings
```json
strings:
	$s0 = "msiexec.exe"
	$s1 = "ReadProcessMemory"
	$s2 = "WinHelpW"
conditions:
	all of ($s*)
```