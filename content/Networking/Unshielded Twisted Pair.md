---
tags:
  - hardware
  - networking
aliases:
  - UTP
excalidraw-plugin:
---
![[Unshielded Twisted Pair-20240716172504044.webp|602]]
These are copper cables which use AWG 22-26 gauge copper twisted to avoid [[Induction]] and encased in a common jacket.
These cables can only travel up to 100m.
Used in [[RJ-11|Telephone Cable]] and [[RJ-45|Ethernet Cable]]
# CAT ratings
They are distinguished between categories(CAT).
These CAT rating determine the voltage, bandwidth, data rate(speed) and distance.
https://tripplite.eaton.com/products/ethernet-cable-types
| Category | Max. Data Rate                         | Bandwidth | Max. Distance                               | Usage                                                     |
| -------- | -------------------------------------- | --------- | ------------------------------------------- | --------------------------------------------------------- |
| CAT 1    | 1 Mbps                                 | 0.4 MHz   |                                             | Telephone and modem lines                                 |
| CAT 2    | 4 Mbps                                 | 4 MHz     |                                             | LocalTalk & Telephone                                     |
| CAT 3    | 10 Mbps                                | 16 MHz    | 100 m (328 ft.)                             | 10BaseT Ethernet                                          |
| CAT 4    | 16 Mbps                                | 20 MHz    | 100 m (328 ft.)                             | Token Ring                                                |
| CAT 5    | 100 Mbps                               | 100 MHz   | 100 m (328 ft.)                             | 100BaseT Ethernet                                         |
| CAT 5e   | 1 Gbps                                 | 100 MHz   | 100 m (328 ft.)                             | 100BaseT Ethernet, residential homes                      |
| CAT 6    | 1 Gbps                                 | 250 MHz   | 100 m (328 ft.)  <br>10Gb at 37 m (121 ft.) | Gigabit Ethernet, commercial buildings                    |
| CAT 6a   | 10 Gbps                                | 500 MHz   | 100 m (328 ft.)                             | Gigabit Ethernet in data centers and commercial buildings |
| CAT 7    | 10 Gbps                                | 600 MHz   | 100 m (328 ft.)                             | 10 Gbps Core Infrastructure                               |
| CAT 7a   | 10 Gbps                                | 1000 MHz  | 100 m (328 ft.)  <br>40Gb at 50 m (164 ft.) | 10 Gbps Core Infrastructure                               |
| CAT 8    | 25 Gbps (Cat8.1)  <br>40 Gbps (Cat8.2) | 2000 MHz  | 30 m (98 ft.)                               | 25 Gbps/40 Gbps Core Infrastructure                       |
### CAT Incompatibility
Higher CAT rated devices will not work if inserted into lower CAT or higher CAT endpoints
Ensure the ports and the cable have the same CAT rating
# Core Types
### Solid Core
The inside of the wire casing is a single wire
![[Unshielded Twisted Pair-20240716201210902.webp]]
- Better conductor
- Stiff and breaks easy
### Stranded Core
Inside of the wire casing is multiple wires
![[Unshielded Twisted Pair-20240716201221767.webp]]
- Worse conductor
- More flexible
# Concepts
- [[Creating Own UTP]]
