---
tags:
  - hardware
  - networking
aliases:
  - I2C
---
A communication protocol used for short distance communications.
- Both master and slave can send/receive data
- [[Point-to-point Communication|Half Duplex]]
# Topology
A master communicates with multiple slaves via:
- SDA bus for data
- SCL wire for clock
- Pull-up resistor connecting to [[Voltage At the Collector|VCC]] or [[Voltage at the Drain|VDD]] to determine the bus speed and power consumption
![[Inter-Integrated Circuit-20250624210201399.webp]]
# Concepts
- [[Inter-Integrated Circuit Protocol|I2C Protocol]]
- [[I2C Modes|I2C Speeds]]