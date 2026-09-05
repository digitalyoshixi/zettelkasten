---
tags:
  - prolog
---
In order to use something, you must define it beforehand.
- Prolog checks file top-to-bottom .
- Prolog reads each line left-to-right.
# Example
```prolog
mylength([_|T], N) :- mylength(T, NT), N is NT+1
```