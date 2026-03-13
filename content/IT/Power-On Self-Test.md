---
tags:
  - os
aliases:
  - POST Program
  - POST
---
When the computer is turned on, the POST program tells all devices to run their built-in diagnostic. The diagnostic result can be relayed in beep codes, text messages or as LED on physical cards.
### Beep Codes
Certain beeping noises will play depending on device status
**No beeps:** Motherboard problem
**2 short beeps:** All is well
**Long beep followed by 2 or 3 short beeps**: Missing video / Motherboard problem
**Indefinitely long beep or strange beep**: Missing [[Random Access Memory|RAM]]
### Text Codes
These vary depending on operating system. It will just tell you the error flat out.
![[Power-On Self-Test-20240525155118579.webp|611]]
### POST Cards
![[Power-On Self-Test-20240525160239484.webp]]
If sound card or graphics card is dead, then you have no other option but to mount a POST led.
It will display a 2-character post code to tell you the issue
# USB POST cards
![[Power-On Self-Test-20240625185653870.webp|228]]
Like regular post expansion cards, but they can be connected via [[Universal Serial Bus|USB]]
# Post POST Handoff
After POST, the [[Basic Input Output System|BIOS]] or [[Unified Extensible Firmware Interface|UEFI]] starts
![[Power-On Self-Test-20260313195422139.webp]]