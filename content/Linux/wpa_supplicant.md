---
tags:
  - linux
  - networking
---
Poor man's [[nmcli]]
# Adding Network
`sudo nvim /etc/wpa_supplicant/wpa_supplicant.conf`
Here is a template config:
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
        ssid= "insert_your_hidden_SSID_here"
        scan_ssid=1
        psk="insert_your_wifi_password_here"
        key_mgmt=WPA-PSK
}
```
The above config applies for hidden networks too.
# Restarting Network
Stupid as fuck.
You need to `reboot` system. There is no service.