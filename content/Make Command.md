---
tags:
  - programming
  - c
---
A command/action ran during a [[Make Rules]].
- Each command is ran in a [[Subshell]] with different environments
# Chaining Commands in Same Subshell
```make
list:
	cd src; ls # two commands in same subshell
```