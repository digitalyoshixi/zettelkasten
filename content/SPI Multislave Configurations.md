---
tags:
  - hardware
  - networking
---
# Independent Slaves
The master node has seperate Chip Select lines for each slave.
![[SPI Multislave Configurations-20250624213353553.webp|389]]
# Cooperative Slaves / Daisy Chain
Every slave will route their output to the next one in the series, and only the last one returns to the master.
![[SPI Multislave Configurations-20250624213437141.webp|388]]