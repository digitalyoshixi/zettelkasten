---
tags:
  - networking
---
![[Cross-Over Cable-20240731180310930.webp|404]]
- Transmit on pins 3,6
- Receive on pins 1,2
Pins on one end do not match pins on the other end.
The ends **do not** need to match [[TIA-568]] specifications.
[[Auto MDI-X]] replaces the need for crossover cables. These days, you will not ever need cross-over cables
# Use Cases
Used for connecting [[Media Device Interface|MDI]] devices to [[Media Device Interface|MDI]] devices or [[Media Device Interface Crossover|MDI-X]] devices to [[Media Device Interface Crossover|MDI-X]] devices. Like:
- [[Switch]] <-> [[Switch]]
- [[Router]] <-> [[Router]]
- Workstation <-> Workstation
- Workstation <-> [[Router]]
# Trancieving & Recieving Protocols
### 10BaseT
![[Cross-Over Cable-20250605145826008.webp|213]]
- [[Network Interface Controller|NIC]] sends through pins 3,6
- [[Network Interface Controller|NIC]] recieves through pins 1,2
### 1000BaseT