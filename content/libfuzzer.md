---
tags:
  - security
  - programming
---
A [[Whitebox Fuzzing]] tool that is integrated with [[Low Level Virtual Machine|LLVM]].
- Adds [[Software Instrumentation|Binary Instrumentation]]
```
clang ./myprogram -fsanitize=fuzzer
```
Run with `./binaryname <corpus_directory>`
# Harness Template
```cpp
int LLVMFuzzerTestOneInput(const uint8_t, *Data size_T Size) {
	uint8_t *buf = malloc(Size);
	memcpy(buf, Data, Size);
	

}
```