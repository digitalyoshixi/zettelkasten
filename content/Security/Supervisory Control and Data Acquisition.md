---
tags:
  - IT
aliases:
  - SCADA
---
![[Supervisory Control and Data Acquisition-20250729030203837.webp|442]]
Systems designed to:
- Manage processes
- Store data
- Establish system backups
- Handle system disruptions and connectivity issues
Used in industrial settings:
- Energy
- Building facilities ([[Heating Ventilation Air Conditioning]])
- Manufacturing
- Logistics
- Industrial
Very big targets for cyber crime.
Often requires [[Network Segmentation]]
# Levels
### Plant Level (Level 0)
Includes physical equipment like [[Sensor]], [[Actuator]], [[Motor]], [[Pump]], etc
### Controller Level (Level 1)
Involves real-time control of physical devices like [[Programmable Logic Controllers|PLC]] that can recieve input from sensors on plan level.
### Coordinating Computer Level (Level 2)
Involves supervisory computers or [[Human Machine Interface|HMI]] systems that provide centralized views of plant operations.
Often collects data from level 1 controllers and display them
### Program Logic Controller Level (Level 3)
Level includes controlling overall production processes.
Includes advanced software systems that can coordinate multiple production lines and log for analysis.