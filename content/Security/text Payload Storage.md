---
tags:
  - security
aliases:
  - .text Payload Storage
---
Storing payload data in the [[.text]] section.
- Has `RX` permissions
- Must be explicitly declared
```c
#pragma section(".text")
__declspec(allocate(".text")) const unsigned char Text_RawData[] = {
	0xFC, 0x48, 0x83, 0xE4, 0xF0, ...
};

int main() {
	// ...
	return 0;
}
```