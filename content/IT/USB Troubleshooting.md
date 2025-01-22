---
tags:
  - hardware
---
Most USB issues come from the fact that manufacturers make USB's which consume too much power or utilize the wrong ports.
# Check Drivers
Certain USB devices like mice or keyboard have extra buttons which the default USB does not support, so make sure you install the drivers.
# Power Mismatch
Error codes may occur when a USB is drawing too much power.
### USB Selective Suspend
You can go to [[Windows Control Panel]], and toggle the USB selective suspend setting to prevent USBs from using power when the computer is off or sleeping.
### USB Low Power
![[USB Troubleshooting-20240704182740892.webp]]
Sometimes the OS will set the USB to low power mode automatically If you dont want this, then go to [[Windows Device Manager]] > Properties > Power Management and uncheck *Allow the computer to turn off this device to save power*.
# USB Permissions
In the [[System Setup Utility|BIOS Menu]], the USB may be disabled, or the USB backwards compatibility is disabled (thus preventing USB 2.0 from being used in 3.0 ports).
# Port Issues
Ensure to port is turned on. The [[System Setup Utility|BIOS Menu]] should be responsible for this, but you can also use [[Windows Device Manager]].
![[USB Troubleshooting-20240704183943863.webp|293]]
The down arrow beside devices means that the port disabled.