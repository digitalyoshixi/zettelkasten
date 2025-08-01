---
tags:
  - networking
---
# nmcli connection
```
sudo nmcli connection add type wifi con-name "eduroam" ifname wlp3s0 ssid "eduroam" --  \          
wifi-sec.key-mgmt wpa-eap \
802-1x.eap peap \
802-1x.phase2-auth mschapv2 \
802-1x.identity "" \
802-1x.password ""
```