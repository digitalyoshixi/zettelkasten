---
tags:
  - networking
  - security
---
# Setup Passwords
![[Cisco IOS Hardening-20260613155655868.webp]]
[[Cisco IOS]] has:
- Console password for console users
- vty password for [[Telnet]] users
- enable password for privileged mode
Can setup with:
![[Cisco IOS Hardening-20260613155914942.webp]]
# Setup Local Users
![[Cisco IOS Hardening-20260613160533956.webp]]
# Setup Access with External Authentication
Using [[Authentication, Authorization, Accounting|AAA]] servers with [[Remote Authentication Dial-In User Service|RADIUS]] or [[Terminal Access Controller Access-Control System Plus|TACACS+]]
![[Cisco IOS Hardening-20260613160840084.webp]]
# Setup [[Secure Shell Protocol|SSH]]
![[Cisco IOS Hardening-20260613161033518.webp]]
You can setup the modulus
```
crypto key generate rsa modulus 1024
```
# Securing WebUI
```
no ip http server
```
```
ip http secure-server
```
```
ip http authentication local
```
```
username name priority 15 password
```
# Enabling IPv4 
```
configure terminal
	interface vlan 1
		ip address <ipaddress> <mask>
		no shutdown
		ip default-gateway <ipaddress>
		exit
ip name-server <ip1> <ip2> ...
```
# Enabling DHCP
```
configure terminal
	interface vlan 1
		no shutdown
		ip address dhcp
```