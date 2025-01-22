---
tags:
  - hardware
---
![[Universal Serial Bus-20240704173814601.webp|394]]
# USB Circuit
The USB host controller is the interface between the system and every USB device that connects to it. It supports up to 127 USB devices (though in reality, most systems just have 6-8 ports).
The host controller:
- Provides power to the connected USB devices
- Sends commands to the USB devices
### USB Shared Resource
As this circuit is shared, the more USB devices that are plugged in, the more work the USB controller has to do, resulting in slower speed and power for each device.
Each USB has a certain # of endpoints, and every USB controller can only support a certain # of endpoints.
If you get a *USB controller resource warning*, then it means too many USB devices are on the same controller. Move some to different controller ports.
# USB Standard Differences
![[USB Host Controller-20240704175702626.webp]]
For each specific USB standard, there requires a different host controller chip to service it.