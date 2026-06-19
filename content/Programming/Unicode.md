---
tags:
  - programming
aliases:
  - UTF-8
  - UTF
  - Wide String
  - Long String
---
An extension of [[ASCII]] encoding. However, it is not limited to only 8 bits to represent characters. [[ASCII]] is not able to display Chinese.
- Unicode uses 16bits. 
# Structure
- The first 128 Unicode characters are [[ASCII]]
- The second 128 Unicode characters are ISO extensions to [[ASCII]]
- Other character sets are spaced out similar to their pre-made conventions.
# Difference From [[Double Byte Character Set|DBC]]
Double byte character set uses 2 bytes.
Unicode does not use 2 bytes, it uses one wide byte.
They both take 16bits per character. But characters in Unicode are treated only as 16bit. 8bit values in Unicode mean nothing.
# UTF-8
Ability to turn a unicode character into 4 bytes. This allows it to be compatible with [[ASCII]] which only reads bytes.
