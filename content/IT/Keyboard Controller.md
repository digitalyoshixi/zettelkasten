---
tags:
  - hardware
---
![[Keyboard Controller-20240524200639347.webp|460]]
These days, it is integrated into [[Chipset]]
# Functionality
![[Keyboard Controller-20240524200813738.webp|474]]
1. Key pressed on the keyboard
2. A scan code corresponding to the key you pressed is sent to the keyboard controller
3. Scan code is saved in keyboard controller's registers
When you need to press multiple keys, the keyboard controller does a binary, tertiary, etc, operation to get the resultant value.
