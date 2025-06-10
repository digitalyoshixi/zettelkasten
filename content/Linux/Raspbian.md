---
tags:
  - raspberrypi
---
On a raspberry pi 2 w, you want a os. get raspbian headless.
1. Download the imager. https://www.raspberrypi.com/software/
2. Get this OS.
![[Raspbian-20231125185948699.webp]]
3. Write it to the sd card.
4. Plug it into your raspberry pi, then plug in your mouse keyboard and then monitor for the initial ssh setup
5. [[Linux SSH Setup]]
change wifi with: `sudo raspi-config` or modify [[dhcpcd]] `/etc/dhcpcd.conf`
