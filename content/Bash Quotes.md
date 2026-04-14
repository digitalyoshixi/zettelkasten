---
tags:
  - programming
  - bash
---
- Double quotes prevent wildcard replacement
- Single quotes prevent wildcard replacement, [[Bash Variables|Variable Substitution]], [[Command Substitution]]
```bash
$ echo Today is `date`
Today is Thu Sep 19 12:28:55 EST 2002
$ echo "Today is `date`"
Today is Thu Sep 19 12:28:55 EST 2002
$ echo 'Today is `date`'
Today is Thu Sep 19 12:28:55 EST 2002
```