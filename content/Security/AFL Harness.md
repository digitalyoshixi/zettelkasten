---
tags:
  - security
  - verification
aliases:
  - AFL++ Harness
  - Libfuzzer Harness
---
# Default
```c
#define SIZE 50

int main() {
	char input[SIZE] = {0};
	ssize_t length = read(stdin, input, SIZE);
	
	// pass input data to functions you want to fuzz
	parser(input, length);
	
	return 0;
}
```
# With `fsanitizer=fuzz`
```c
int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) { 
	// pass input data to functions you want to fuzz
	parser(data, size)
	
	return 0;
}
```
