---
tags:
  - networking
aliases:
  - APIPA
---
If a device cannot receive an [[IP Address]] from [[Dynamic Host Configuration Protocol|DHCP]] due to: 
- No DHCP server found
- Duplicate IP addresses (there can only be one)
The [[Internet Assigned Numbers Authority]] grants an IP address from `169.254.0.1` to
`169.254.255.254` to give to the device.
All APIPA addresses can only communicate with other APIPA addresses in the same subnet `169.254.*.*`, so they disconnected from [[The Internet]]