---
tags:
  - networking
  - networking
aliases:
  - CRC
  - CRC Checksum
---
A [[n-Error Detecting Code]] used in the [[Ethernet Protocol]] to determine if any errors occurred during data transmission. 
Can be used as a [[Error Correcting Codes|ECC]] with [[Bitfilter]].
A CRC can be:
- 8 bits
- 16 bits
- 32 bits
![[Cyclic Redundancy Check-20240716162152283.webp|580]]
Often put at the end of a packet frame
# Concepts
- CRC algorithm finder: https://crccalc.com/?crc=123456789&method=&datatype=ascii&outtype=hex
- [[reveng]]
# Similar Methods
- [[Frame Check Sequence|FCS]]