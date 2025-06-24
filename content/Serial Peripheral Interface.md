---
tags:
  - hardware
  - networking
aliases:
  - SPI
---
A 4-wire [[Serial Communication]] protocol developed by [[Motorola]].
Similar to [[Inter-Integrated Circuit|I2C]] and [[Universal Asynchronous Receiver Transmitter|UART]].
- [[Point-to-point Communication|Full Duplex]]
Often used to transfer data between a smart controller and less smart peripheral device (sensors, clocks, controllers).
# Topology
A master node is connected to one or more slaves with 4 wires between them.
![[Serial Peripheral Interface-20250624211909567.webp|411]]
- Chip Select(CS) : Chooses communication target. [[Active Low Notation|Active Low]]
- Synchronous Clock(SCLK) : Provides timing
- Master Out Slave In(MOSI) : Data transmitted by master
- Master In Slave Out(MISO): Data recieved by master. Not required in one-way communication (i.e Displays)
# Concepts
- [[Serial Peripheral Interface Protocol]]
- [[Clock Polarity]]
- [[Clock Phase]]
- [[SPI Modes]]
- [[SPI Multislave Configurations]]