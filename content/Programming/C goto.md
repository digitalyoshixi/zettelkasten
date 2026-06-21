---
tags:
  - c
---
YESSS!
MY BAYBAY IS HERE!
```c
goto label_name;

label_name:
	// some actions here
```
- [[C labels]]
# goto use cases
### Inescapable Nested Loop
```c
for (...)
	for (...){
		if (disaster)
			goto error;
	}
```
when inside of a loop, how do you break out of its parent loop?
Well, you can add conditions and a custom boolean i guess if you want to be lame
or you can use a goto statement!
# Problems with goto
- Breaks stack
- Requires you to rewrite entire code to make control flow possible