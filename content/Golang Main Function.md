---
tags:
  - go
---
# Symbol
Golangs main function has symbol `main.main`
# Routine
```c
0049ee00    int64_t main.main.func3(int64_t arg1, int64_t arg2, void* arg3, void* arg4 @ r14)

0049ee00    {
0049ee00        int64_t var_b8;
0049ee0c        int64_t rbp;
0049ee0c        
0049ee0c        if (&var_b8 <= *(uint64_t*)((char*)arg4 + 0x10))
0049ee0c        {
0049f0c0            runtime.morestack.abi0(arg1, arg2, arg3, rbp);
0049f0c0            /* no return */
0049ee0c        }
0049ee0c        
```
main function will check if the current stack pointer is above the maximum. If not, then the program will continue running as normal.