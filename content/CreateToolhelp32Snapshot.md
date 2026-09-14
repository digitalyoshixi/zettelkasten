---
tags:
  - win32api
  - programming
  - windows
---
```c
HANDLE CreateToolhelp32Snapshot(
	[in] DWORD dwFlags,
	[in] DWORD th32ProcessID,
)
```
- `dwFlags` as `TH32CS_SNAPPROCESS` should instruct function to include process info in the snapshot, set `th32ProcessID` to `0`
- On success, returns snapshot handle
- On failure, returns `INVALID_HANDLE_VALUE`