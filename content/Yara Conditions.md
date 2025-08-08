---
tags:
  - malware
  - security
---
Specific conditions for a rule to be fired.
```json
condition:
	(condition1 and condition2) or
	not (condition3 xor condition4)
```
# Conditions Guides
- [[Yara Instant Match]]
- [[Yara String Match Conditions]]
- [[Yara File Size Conditions]]
- [[Yara Quantity Conditions]]
# Yara Keywords
|          |           |            |          |             |          |            |           |
| -------- | --------- | ---------- | -------- | ----------- | -------- | ---------- | --------- |
| all      | and       | any        | ascii    | at          | base64   | base64wide | condition |
| contains | endswith  | entrypoint | false    | filesize    | for      | fullword   | global    |
| import   | icontains | iendswith  | iequals  | in          | include  | int16      | int16be   |
| int32    | int32be   | int8       | int8be   | istartswith | matches  | meta       | nocase    |
| none     | not       | of         | or       | private     | rule     | startswith | strings   |
| them     | true      | uint16     | uint16be | uint32      | uint32be | uint8      | uint8be   |
| wide     | xor       | defined    |          |             |          |            |           |