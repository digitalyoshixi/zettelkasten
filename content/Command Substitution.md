---
tags:
  - programming
aliases:
  - Bash Quotes
---
A capability in [[Bash Programming|Shell Programming]] that allows grabbing the output of a command by spawning a [[Subshell]].
```bash
echo `ls`
echo $(ls)
```
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