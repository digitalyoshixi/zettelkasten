---
tags:
  - windows
  - malware
---
Specialized bundle of software for windows systems designed for malware analysts
# Windows VM Installation
Follow [[Windows 10 Installation]], then:
1. Install gpedit.msc 
	![[FlareVM-20240401185029736.webp]]and open it `gpedit`
2. Local Computer Policy > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Turn Off Microsoft Defender Antivirus > Enable
3. Local Computer Policy > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Real Time Protection > Turn Off Realtime Protection > Enable
4. Local Computer Policy > Administrative Templates > Windows Components > Windows Update > Configure Automatic Updates > Disable
5. https://github.com/jeremybeaume/tools disable defender
6. Restart VM
7. Make a snapshot
8. Install FlareVM https://github.com/mandiant/flare-vm
9. Change network option to only be connected to host

