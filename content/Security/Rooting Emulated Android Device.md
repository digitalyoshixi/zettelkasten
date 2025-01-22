---
tags:
  - android
  - reverse_engineering
---
1. `git clone https://github.com/newbit1/rootAVD.git`
2. `cd rootAVD`
3. `./rootAVD.bat ListAllAVDs` or `./rootAVD.sh ListAllAVDs` if its linux. See the android device you want to root
   ![[Rooting Emulated Android Device-20240901022832607.webp]]
4. Run the command `rootAVD.bat system-images\<yourandroid>\google_apis_playstore\x86_64\ramdisk.img`
5. The [[Android Virtual Device|AVD]] will shut down, restart it in android device manager
   ![[Rooting Emulated Android Device-20240901023126685.webp]]
6. Run [[Magisk]]. If it requires extra setup and restart then allow it
   ![[Rooting Emulated Android Device-20240901023244632.webp|375]]
7. `adb shell`, and then type `su`, go to magisk app and grant permission. You are now root