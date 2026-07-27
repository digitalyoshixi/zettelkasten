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
# Concepts
- [[AFL Harness]]
# Usage
### Compile Harness with Instrumentation
```
afl-cc myprogram
```
### Compile Harness with Instrumentation Assembly Level
- This is what afl-cc does under the hood (only part where instrumentation is setup)
```
afl-as myprogram.s
```
### Fuzz Harness
```
afl-fuzz -i ./corpusdir -o ./out -s 1337 ./install/bin/pdftotext @@
```
- `-i` is the corpus directory
- `-o` is the directory that AFL++ stores mutated files
- `-s` is the static random seed to use
- `@@` is the placeholder target AFL substitutes for each file name in corpus
### Fuzz with Custom Syntax-Aware Dictionary
AFL is good for raw binary formats but not so much text formats ([[JSON]], [[Hypertext Markup Language|HTML]], etc) so sometimes you define custom symbols to use:
```
afl fuzz -i in -o out -x testcase/json.dict ./jq @@
```
Example dict:
```json
"<="
"->"
"alignas"
"alignof"
"and"
"and_eq"
```
### Corpus Minimizer
Attempts to find smallest set of test cases from existing cases that will still have the widest coverage
Minimize corpus directory:
```
afl-cmin -i testcase_dir -o testcase_out_dir -- /fuzzed_program
```
Minimize single test case:
```
afl-tmin -i testcase -o testcase_out_dir -- /fuzzed_program
```
### Setup [[tmpfs]]
```
sudo mount -t tmpfs -o size=2000m tmpfs /mnt/fuzzing
```