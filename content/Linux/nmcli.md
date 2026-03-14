---
tags:
  - networking
  - linux
aliases:
  - Linux Connect To Network
---
A tool that comes prepackaged with [[NetworkManager]]
Alternative to [[wpa_supplicant]]
# Connecting to network
https://www.youtube.com/watch?v=tLLTjsgIpYY&embeds_referring_euri=https%3A%2F%2Fduckduckgo.com%2F&feature=emb_logo

1. `sudo systemctl start NetworkManager`
2. `nmcli dev status` if your wireless device is up, then you can connect. if not then, follow these steps:
	1. `rfkill` or `sudo rfkill` and enable the wireless device
	2. `sudo ip link set yourwirelessdeivce up`
3. `nmcli device wifi list` find all connectable networks. remember that SSID
4. `nmcli dev wifi connect SSID password THEPASSWORD`
5. reboot if its your first time. `ping gnu.org` to check if it works

# Connecting to school network
https://www.reddit.com/r/archlinux/comments/pb3r0f/cannot_connect_to_college_wifi_using/
- `nmcli connection add type wifi con-name "CampusWifi" ifname wlan0 ssid eduroam`
- `nmcli connection edit CampusWifi`
- `set 802-1x.eap peap`
- `set 802-1x.phase2-auth mschapv2`
- `set 802-1x.identity _yourUsername_`
- `set 802-1x.password _yourPassword_`
- `set wifi-sec.key-mgmt wpa-eap`
- `save`
- `activate`
*you might need to set 802.11... SSID*

# DNS Changing
- `nvim /etc/resolv.conf`
- Remove the google DNS and add your own
- Set the file to have [[chattr|Immutable File Attribute]] with `chattr +i /etc/resolv.conf`
- `sudo systemctl restart NetworkManager`
# Disable IPv6
Sometimes in DNS can be bypassed with IPv6. To stop this, you must disable ipv6.
![[nmcli-20240218174853302.webp]]
![[nmcli-20240218174906242.webp]]
- `nmcli connection show`. Get the network name
- `nmcli connection modify "network name" ipv6.method "disabled"`
- `sudo systemctl restart NetworkManager`