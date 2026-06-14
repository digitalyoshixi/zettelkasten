---
tags:
  - verification
  - security
aliases:
  - AFL
  - AFL++
---
A [[Fuzzing|Fuzzer]] developed by google, improved after the original AFL was deprecated in 2017.
- Has a wrapper for [[GCC]] (`afl-cc`)
- Adds [[Software Instrumentation]]
	- `__AFL_FUZZ_INIT()` - start fuzzing
	- `__AFL_FUZZ_TESTCASE_YOURNAME()` - fuzzing tag
	- `__AFL_LOOP(1000)` - loop fuzzer this many times
# Usage
```
afl
```