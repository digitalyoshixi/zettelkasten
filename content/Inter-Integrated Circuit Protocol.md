---
tags:
  - hardware
  - networking
aliases:
  - I2C Protocol
---
# Protocol
![[Inter-Integrated Circuit-20250624210247901.webp]]
1. The protocol starts when a node's SDA and SCL are both low. This node will then become the master, and is responsible for sending clocks
2. The master must then specify which node to talk to during the slave address window. Usually 7 bits long.
   ![[Inter-Integrated Circuit-20250624210500174.webp]]
   During this time, SDA only changes when SCL is low
3. A read or write bit is sent.
	- 0 -> Master wants to write data to slave
	- 1 -> Master wants to read data from slave
4. A acknowledgement bit is sent in response
	- 0 -> acknowledgement (ACK)
	- 1 -> negative acknowledgement (NACK)
	 This circuit is idle high, so no response will default to NACK
5. The data byte is sent if the acknowledgement is 0. All subsequent data sent must also have acknowledgements.
   ![[Inter-Integrated Circuit-20250624210959521.webp]]
6. Stop condition occurs when both SCL and SDA remain high, signalling an idle bus.
   ![[Inter-Integrated Circuit-20250624211127877.webp|359]]