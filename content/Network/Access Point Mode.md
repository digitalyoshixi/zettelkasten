---
tags:
  - networking
aliases:
  - AP Mode
  - Master AP Mode
---
A [[Network Interface]] mode exclusive for [[WI-FI|IEEE 802.11]] [[Network Interface Card|WNIC]].
Allows the interface to act as a [[Access Point|AP]].
- Can send [[Basic Service Set|BSS]] beacons
Used in [[Hotspot|Wifi Hotspot]]
# Setup
```
iw dev wlan0 interface add ap0 type __ap
```