---
tags:
  - networking
---
![[Cisco IOS Interface Counters-20260620161521835.webp]]
# Fields
- **Runts**: Frames that did not meet minimum frame size (64 bytes)
- **Giants**: Frames that exceed maximum frame size (1518 bytes)
- **Input Errors**: total counter including runts, giants, no buffer, CRC, frame, overrun, ignored counts
- **CRC**: recieved frames that did not pass [[Frame Check Sequence|FCS]] math
- **Frame**: recieved frames that have an illegal format
- **Packets Output**: total number of frames forwarded out interface
- **Output Errors**: # of frames switch tried to transmit, but a problem occured
- **Collisions**: # of collisions that occur when interface transmitting frame
- **Late Collisions**: Subset of collisions that happen after 64-th byte of frame has been transmitted, often point to [[Duplex Mismatch Issue]]