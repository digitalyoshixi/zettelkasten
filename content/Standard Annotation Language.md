---
tags:
  - security
  - verification
aliases:
  - SAL
---
A language for annotating [[C++]] code and libraries.
- Can be used to improve results of [[PREfast]]
# Example
```c
void memcpy( _Out_cap_(count) char* dest,
			 _In_count_(count) char* src,
			 size_t count);
```
- `_Out_cap_(count)` specifies that p will write `len` bytes to memory at `dest`
- `_In_cap_(count)` specifies that p will read `len` bytes to memory at `src`
# Annotations

### Functions
- `_Check_return_`: caller must check return value of this function
- `[SA_Post(MustCheck=SA_Yes)]`: same as `_Check_return_`
### Parameters
- `opt_`: parameter may be null
- `[SA_Pre(NULL=SA_NO)]`: requires non-null parameter
- `[SA_Pre(Tainted=SA_YES)]`: This argument is tainted
### Parameters (Buffers)
- `_In_`: function reads from buffer. Caller must provide buffer and initialize
- `_Inout_`: function reads and writes to buffer. Caller must provide buffer and initialize
- `_Out_`: function writes to buffer. Caller must provide buffer, function will initialize
- `cap_(size)`: writable size in elements
- `bytecap_(size)`: writable size in bytes
- `count_(size)`: readable size in elements
- `bytecount_(size)`: readable size in bytes