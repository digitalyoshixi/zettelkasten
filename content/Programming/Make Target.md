---
tags:
  - programming
  - c
aliases:
---
This is a identifier for a specific series of commands.
```c
# target with dependencies for other targets
# runs clean, then dirclean
fullclean: clean dirclean

clean:
	rm -rf ./build

dirclean:
	rmdir ./build

# running command without writing to stdout
hello:
	@echo "Hello"
```