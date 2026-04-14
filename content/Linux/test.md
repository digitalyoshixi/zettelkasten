---
tags:
  - linux
---
A command used to return 0 or 1 as an [[Exit Codes]].
```bash
$ test 2 -lt 3
$ echo $?
0
$ test 3 -lt 3
$ echo $?
1
```
# Numerical Comparisons
```bash
$a -lt $b # a < b
$a -gt $b # a > b
$a -le $b # a <= b
$a -ge $b # a >= b
$a -eq $b # a == b
$a -ne $b # a != b
```
# String Comparissons
```bash
"$a" = "$b" # a is same as b
"$a" == "$b" # a is same as b
"$a" != "$b" # a is not same as b
-z "$a" # length of a is zero
-n "$a" # length of a is non-zero
```
# Entity Comparissons
```bash
-d filename # exists as a directory
-f filename # exists as a regular file
-r filename # exists as readable
-w filename # exists as writable
-x filename # exists as executable
-z string # exists as emptystring

```