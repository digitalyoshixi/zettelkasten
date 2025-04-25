---
tags:
  - os
aliases:
  - I/O
---
Most of the operating system code is dedicated to managing input and output.

An I/O device is connected to the machine via I/O port. Like usb,hdmi,serial ports. Each input output device has a controller that maintains local buffer storage and special purpose registers.

The device controller is nothing but intermediate hardware between the machine, device and OS. The OS -> CPU -> device controller.

The only way the CPU can communicate with the device manager is by talking to the device driver.

**Driver and OS are both loaded on the same memory, but they are not part of each other**

The driver and OS can both receive and send data to each other.

You can think of a driver as a daemon(background) program, which resides in the memory space until the system shuts down.

Above all, is why I/O devices (those shiny RGB keyboards) stop working as soon as driver program crashes.