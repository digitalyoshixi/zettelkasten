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
- Adds [[Software Instrumentation]] that works with [[DynamoRIO]] and [[Pintools]]
	- `__AFL_FUZZ_INIT()` - start fuzzing
	- `__AFL_FUZZ_TESTCASE_YOURNAME()` - fuzzing tag
	- `__AFL_LOOP(1000)` - loop fuzzer this many times
![[American Fuzzy Lop-20260625005741354.webp]]
# Usage
### Compile Harness with Instrumentation
```
afl-cc myprogram
```
### Fuzz Harness
```
afl-fuzz -i ./corpusdir -o ./out -s 1337 -- ./install/bin/pdftotext @@ ./out
```
- `-i` is the corpus directory
- `-o` is the directory that AFL++ stores mutated files
- `-s` is the static random seed to use
- `@@` is the placeholder target AFL substitutes for each file name in corpus
