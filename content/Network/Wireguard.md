---
tags:
  - networking
---
A better version of [[OpenVPN]]
It has better throughput, quicker speeds and more security.

# Raspberry Pi Installation
https://raspberrytips.com/install-wireguard-raspberry-pi/
### Server-Side
We are using PIVPN.
`curl -L https://install.pivpn.io | bash`
Choose wireguard. It will guide you through the others
Ensure port `51820` or whatever you set as the port is enabled in [[Uncomplicated Firewall|ufw]]
### Create Users
On the server, when you want to add a user, do: 
`pivpn add`
It will generate a `.conf `file. Be sure to transfer this file to your client computer. I would just ssh into the box and cat the file, paste it in notepad and save.
### Install Wireguard Client
https://www.wireguard.com/install/ 
Click 'import tunnel' and open the `.conf` file you just copied

My public ip is 207.188.72.19

# Modify Port
`wg-quick down wg0`
`sudo nvim /etc/wireguard/wg0.conf`
change the listening port to whatever port u like.
`wg-quick up wg0`
