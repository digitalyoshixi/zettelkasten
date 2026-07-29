---
tags:
  - security
aliases:
  - .data Payload Storage
  - .rdata Payload Storage
---
Payloads stored in the [[Data Section|.data]] section.
- Has a `RW` region
- Immediately detectable by [[Memory Scanner]]
```c
unsigned char Data_RawData[] = {
	0xFC, 0x48, 0x83, 0xE4, 0xF0, ...
}

int main(){
	return 0;
}
```