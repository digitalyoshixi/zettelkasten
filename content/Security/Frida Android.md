---
tags:
  - security
---
You require a [[Android Rooting|Rooted]] android phone to use frida, or an android emulator with [[Android Debug Bridge|adb]]
# Client Installation
- Refer to [[Frida]]
# Server Installation
### [[Android Virtual Device|AVD]] Setup
1. Check the CPU architecture of the AVD device
   ![[Frida-20240901024636491.webp]]
2. Download the correct server release off https://github.com/frida/frida/releases
   ![[Frida-20240901024741197.webp]]
3. Unzip the xz file 
   ![[Frida-20240901024937522.webp]]
4. `adb push <fridaserverfile> /data/local/tmp`
   ![[Frida-20240901025147843.webp]]
5. `adb shell`
6. `su`
7. `cd /data/local/tmp`
8. `chmod 755 <fridaserverfile>`
9. `./<fridaserver> &`
# Starting Frida 
1. Use [[Blutter]] to create `blutter_frida.js`
2. Modify `blutter_frida.js` to remove the warning and to modify the hook
   ![[Frida-20240901030834061.webp]]
### Emulated Device
3. Run the app on the emulator
4. `frida-ps -Ua` to view appname
   ![[Frida-20240901030316003.webp|553]]
5. `frida -U <appname> -l blutter_frida.js`
# Tools
- `frida-ps -U` - show all running processes
- `frida-ps -Ua` - show all running applications
- `frida-ps -Uia` - show all running and not running applications
- `frida -U -f <app>.apk -l <script>.js`
# Frida Commands
- `Module.enumerateExports("libapp.so")`- prints all the exported functions and variables along with their address in memory
  ![[Frida-20240901032144321.webp]]