---
tags:
  - malware
---
You can just find these with [[xxd]]
# Fixed Length
```json
strings:
	$mz = {4d 5a}
```
# Array with Arbitrary Sequence
```json
strings:
	// jump assembly instruction, match any address 4-6 bytes long
    $hex_string = { F4 23 [4-6] 62 B4 }
```
Will match any of these:
![[Yara Byte Array-20250807234846551.webp]]
```json
strings:
	// jump assembly instruction, match any address 6 bytes long
    $hex_string = { F4 23 [6] 62 B4 }
```
# Array with Wildcard
```json
strings:
	// match a specific byte sequence wiht a wildcard
	$arr_with_wildcard = {70 74 ?? 25 3E}
```