---
tags:
  - windows
---
# Specific
- [[Windows Active Directory Troubleshooting]]
# Rebooting System
As a system runs, programs may cause memory leaks or certain services cause issues.
It is best to reset all programs by rebooting
# System File Check
Run [[Windows System File Checker]] to see if all system files are correct
# Reinstall Applications
Certain programs may be incompatable with the OS, or may have patches fixed in the newest release.
# Hardware Upgrade
See if your hardware meets the system's requirements
# Windows Recovery Environment
You can create this with a windows installation drive
Allows you to:
- [[Windows System Restore]]
- Startup settings
- Uninstall updates
- System Image Recovery
- [[Windows Startup Repair]]
- Command Prompt
- UEFI Firmware Settings
- Reset the PC. You can keep files or remove everything and reinstall from scratch
# [[Rebuild Windows Profiles]]

# Frequent BSOD/Stop Error
Caused by:
- Fast startup not loading drivers
- Driver problems
- Issues with current OS version
To solve:
- Check the error message or [[Windows Event Viewer]]
- Try running in [[Windows Safe Mode]] to see if its a driver issue
- Remove recently installed hardware
- Run hardware diagnostics
- F8 and boot to last known good configuration
- Run a [[Preinstallation Environment|PE]] and then use repair tools
- Use [[Windows Startup Repair]]
# Services Not Starting
- Go to Services and then configure the service behavior to be enabled
- Bad Driver
- Bad Hardware
- Check account permissions
- Reinstall the application
- Check system files
# Memory Warnings
![[Windows Troubleshooting-20240822005032184.webp]]
- Close programs 
- Install more RAM
- Use [[Virtual Memory]]
# USB Controller Resource Warnings
![[Windows Troubleshooting-20240822005246896.webp]]
Too many USB endpoints are being occupied. 
- Change the USB ports plugged in around. USB 2.0 interfaces support more endpoints
- Remove USBs
# System Instability
Frequent software errors, system hangs, application failures.
- Determine with [[Windows Reliability Monitor]]
- Run hardware diagnostics
- Run [[Windows System File Checker]]
- Run [[Anti-Malware Software]] scans

# No OS Found (Boot BCD Errors)
1. Check if you left a bootable USB drive in the ports
2. Check boot order priority in BIOS
3. Use [[Windows Startup Repair]]
4. Manually reconfigure system with `bootrec /rebuildbcd`
5. Check to see if partition is set as active
# Time Desync
The system time automatically syncs once a week to http://time.windows.com/. If it doesn't, then you can manually resync time in settings or manually adjust time.
# Sluggish Performance
- Kill tasks in [[Task manager]]
- Defrag disks with [[Windows Disk Defragmenter]]
- [[Windows Updates]] to get new drivers
- PC is in power saving mode
- PC is overheating
- [[Anti-Malware Software]] is busy
# Application Crashes
- Check [[Windows Event Viewer]]
- Check [[Windows Reliability Monitor]]
- Reinstall application
# No Errors in [[Windows Event Viewer]]
Not caused by any software issue.
Run hardware diagnostics
# Missing [[NTLDR]]
This means the boot loader is missing or corrupt.
Fix it by:
- Running [[Windows Startup Repair]]
- Disconnecting all [[USB Flash Drive]]
- Try running [[Windows Safe Mode]]
- Replacing the NTLDR file with a good version copied from another OS with the same version
# Driver Failure
1. Enable boot logging from [[Windows System Configuration|msconfig.exe]]
2. Boot in [[Windows Safe Mode]]
3. Analyze the ntbtlog.txt file