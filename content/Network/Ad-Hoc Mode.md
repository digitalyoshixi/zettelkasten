---
tags:
  - networking
aliases:
  - IBSS
  - Peer-to-Peer Ad-Hoc Mode
---
A [[Network Interface]] mode exclusive to [[WI-FI|IEEE 802.11]] [[Network Interface Card|WNIC]] that allows for peer-to-peer without a [[Access Point|AP]].
- All stations equal direct communication
- Uses [[Basic Service Set|BSS]] beacons
# Setup
```
iw dev wlan0 set type ibss essid MyNet
iw dev wlan0 ibss join MyNet 2412
```