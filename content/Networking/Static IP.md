---
tags:
  - networking
---
You can manually set the IP address on your local computer without ever communicating with a [[Dynamic Host Configuration Protocol|DHCP]] server.

https://www.cyberciti.biz/faq/add-configure-set-up-static-ip-address-on-debianlinux/

Alternatively, you can reserve an ip with [[DHCP reservation]]. This achieves the same effect, but it requires you to have access to the server.

# Debian Static IP
On debian linux.
1. backups. `sudo cp /etc/network/interfaces /root/`
2. Get nameservers. `grep "nameserver" /etc/resolv.conf`
3. be sure to add the following lines:
```c
# the primary network interface
auto enp0s3
iface enp0s3 inet static
	address your_address
	netmask 255.255.255.0
	gateway your_gateway
	dns-nameesrvers name_server_1 name_server_2
```
![[Static IP-20240211043423576.webp]]

# Raspbian Static IP
`sudo nvim /etc/dhcpcd.conf`
Add the following if there wasn't already
```
interface wlan0
	static ip_address=66.212.170.220/24
	static routers=66.212.170.217
	static domain_name_servers = 8.8.8.8 8.8.4.4
```
