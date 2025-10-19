---
tags:
  - networking
---
# Leasing
All IP addresses are leased and will be revoked unless renewed.
By default this lease is 8 days
2 Timers will check if devices want renewed leases.
### T1 Timer
- Checks at 50% of the lease time if the device wants to renew
### T2 Timer
- Checks at 87.5% of the lease time if the device wants to renew
- Used for redundancy incase the DHCP goes down temporarily