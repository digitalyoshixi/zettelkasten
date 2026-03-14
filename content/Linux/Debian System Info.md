---
tags:
  - debian
  - linux
  - os
---
https://vitux.com/get-debian-system-and-hardware-details-through-the-command-line/
We want to view hardware info like RAM, cpu rate, cores, etc.
To do so, we first need to install the lshw package.
`sudo apt-get install lshw`
and then just type command:
`sudo lshow -short` to view the shortened version.
