---
tags:
  - raspberrypi
  - projects
---
A DNS server you can setup on your raspberry pi.
# Installation
1. SSH into your raspberry pi
2. Ensure the raspberry pi has a [[Static IP]]
3. `curl -sSL https://install.pi-hole.net | bash`
When finished, set each device's dns to be PI-hole.
[[Windows DNS Changing]]

# Adlists
When you finished setting up pihole, when you should be given a password. note that down. Then go to `theipofyourraspberrypi` in your browser to enter the webportal.

`pihole -g` to update adlists