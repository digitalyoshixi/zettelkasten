---
tags:
  - networking
  - forensics
---
A [[Command Line Interface|CLI]] for [[Wireshark]].
# Export All Packets Based off Filter
```
tshark -r KaptenStrang.pcap -Y "ip.src == 192.168.0.9 and ip.dst == 10.2.0.2 and tcp.len > 5000" -T fields -e tcp.payload | xxd -r -p > out.binary
```