---
tags:
  - networking
aliases:
  - Line Status
  - Protocol Status
---
These are status codes returned by `show interfaces` command in [[Cisco IOS]]
# Line Status
Describes [[OSI Physical Layer|OSI Layer 1]] status
# Protocol Status
Describes [[OSI Data Layer|OSI Layer 2]] status
# Table

| Line Status           | Protocol Status     | Interface Status | Typical Root Cause                                                                                                                                                 |
| --------------------- | ------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| administratively down | down                | disabled         | The **shutdown** command is sedt                                                                                                                                   |
| down                  | down                | notconnect       | - No cable<br>- bad cable<br>- wrong cable pinouts<br>- MDIX disabled<br>- speed mismatch<br>- neighboring device is powered off, **shutdown**, or error disabled. |
| up                    | down                | notconnect       | Not expected on LAN switch physical interfaces.                                                                                                                    |
| down                  | down (err-disabled) | err-disabled     | Port security (or other feature) has disabled the local interface.                                                                                                 |
| up                    | up                  | connected        | The interface is working.                                                                                                                                          |
