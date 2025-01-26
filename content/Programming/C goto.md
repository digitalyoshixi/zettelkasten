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

[[C labels]]

**goto is a feature you may never need to use in your life**

but its a niche feature thats really cool

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
**NO DONT USE A GOTO STATEMENT**

# Problems with goto
- Breaks stack
- requires you to rewrite entire code to make control flow possible