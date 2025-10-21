---
tags:
  - linux
---
# Arch Add to sudoers file
3. `usermod -aG wheel,audio,video,optical,storage david`
4. `visudo`
5. uncomment the line `%wheel ALL=(ALL:ALL) ALL`
6. add the line `Defaults !tty_tickets``