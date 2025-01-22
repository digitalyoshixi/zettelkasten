---
tags:
  - synchronization
---
Syncthing is a syncing software that is decentralized, utilizing peer to peer protocols to transfer files.
This means, you can sync files without every using a server.

All you need to do is install syncthing on all your devices, then go to the webui.

# Installation (Windows or Arch)
Download syncthing with pacman, or on windows, download it through the webpage: https://syncthing.net/downloads/
Run the exe or type the command `syncthing`
You will be brought to this webpage.
![[Syncthing-20231125202348062.webp|589]]
Its always the same. 127.0.0.1:8384

# Configuring Sync
Dont bother setting up a username and password
Go down here on your 'non-main' device.
![[Syncthing-20231125203915146.webp]]
![[Syncthing-20231125203922082.webp]]
Then, on the other device, add that code in here
![[Syncthing-20231125204010334.webp]]
![[Syncthing-20231125204027545.webp]]
Alright, its connected now
![[Syncthing-20231125204057868.webp]]

# Sharing Folders
Make a folder, then edit it
![[Syncthing-20231125204405854.webp|498]]
Make sure the path is correct
![[Syncthing-20231125204431098.webp|402]]
then go to Sharing and select your homie
![[Syncthing-20231125204455143.webp]]
Then on the other computer, click 'Add' and then rename that folder path.
![[Syncthing-20231125204615569.webp]]
# Windows Autostart
If you want to Syncthing client to start on system boot.
1. Open [[Windows Task Scheduler]]![[Syncthing-20240303214752207.webp]]
2. Make a new task, ![[Syncthing-20240303214921118.webp]]![[Syncthing-20240303214845050.webp]]
3. Allow the task to be ran automatically when user logs in
![[Syncthing-20240303215613721.webp|441]]
5. Make the action run syncthing wherever it is located with the arguments `--no-console --no-browser`
![[Syncthing-20240303215509457.webp|514]]
6. In the settings, uncheck the stop task after ...
![[Syncthing-20240303215729275.webp|498]]
