---
tags:
  - windows
---
A [[Win32 API]] function to convert a string version of [[IPv6]] into the binary version.
```c
NTSYSAPI NTSTATUS RtlIpv6StringToAddressA(
  [in]  PCSTR    S,
  [out] PCSTR    *Terminator,
  [out] in6_addr *Addr
);
```
- `[in] S`: pointer to buffer containing the C-string representation of the IPv6 address.
- `[out] Terminator`: Receives a pointer to the character that terminated the converted string
- `[out] Addr`: A pointer where the binary representation of the IPv6 address is to be stored.