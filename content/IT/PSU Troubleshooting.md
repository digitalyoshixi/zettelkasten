---
tags:
  - hardware
aliases:
  - PSU Tester
---
# Sufficient Wattage
If the computer wont turn on or does not work properly, try removing a component or seeing if the [[PSU Wattage Rating]] is sufficient enough for all your components.
# Bad Outlet
Use the outlet test with a [[Multimeter]] to see if electricity can get to the power supply.
# PSU Continuity Test
Use a [[Multimeter]] at 5V to check the voltages coming out of the power supply.
![[PSU Troubleshooting-20240627154444298.webp|304]]
The voltage read does not need to be exactly its nominal value. It can vary $\pm 10\%$ of its stated value.
This means a 12V line can vary from 10.8V - 13.2V.
Test every connection to the power supply that is connected to a peripheral with the multimeter set a 20V DC.
# PSU Tester
If you dont have a motherboard, but you still want to test if the PSU works, then you can purchase a PSU tester.
![[PSU Troubleshooting-20240627155356549.webp|276]]
the above example is a tester for [[ATX12V 2.0 PSU]].
# PSU Internal Electronic Failure
When PC problems are intermittent, this may signal that the PSU is dying. These intermittent problems include:
- Several boots to start working
- Random Error codes that are one-off
- Intermittent locking
- Repeated USB replugging before it can be identified
PSU break in computer more often than any other component
# Fuse Popping
Every PSU has a fuse, that may pop if given a strong current.