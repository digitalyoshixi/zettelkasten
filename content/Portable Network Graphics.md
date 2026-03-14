---
tags:
  - file
aliases:
  - PNG
---
A [[Structured Object File Format]] for images.
# File Format
![[Portable Network Graphics-20260313130658897.webp]]
### Header
##### CRLF Signatures
8-byte signature: `89504e470d0a1a0a`
- `89`: Detect transmission system that do not support 8-bit data
- `50 4e 47` : `PNG` magic number
- `0D 0A` : DOS-style [[Carriage Return Line Feed|CRLF]]
- `1A` : byte that stops display of file when DOS command [[DOS type]] is used
- `0A` : Unix style [[Line Feed|LF]] to detect unix-DOS line end conversion
##### Extra
- Header Length (4-bytes) (often 13)
- IHDR (4-bytes)
- Width (4-bytes)
- Height (4-bytes)
- Bit-depth flag (1-byte)
- Color-type flag (1-byte)
- Compression flag (1-byte)
- Filter flag (1-byte)
- Interlacing flag (1-byte)
- [[Cyclic Redundancy Check|CRC]] (4-byte)
### Chunks
- Chunk length (4-bytes)
- Chunk Type (4-bytes)
	- IDAT (data)
	- IEND (final chunk)
- Chunk data
- [[Cyclic Redundancy Check|CRC]] (4-byte)