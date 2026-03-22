---
tags:
  - networking
---
A limit to how much data can be sent before recieving a ACK response during [[Transmission Control Protocol|TCP]] communication.
# Flow Control (Dynamic Window Size)
![[TCP WIndow Size-20260322014338874.webp]]
The receiver can dynamically change their window size by sending a new packet with the window size field changed.
If they set it to 0, it forces the sender to wait until the next ACK response.