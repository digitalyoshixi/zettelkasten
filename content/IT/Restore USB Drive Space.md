---
tags: []
---
Certain times, when creating bootable drives, the partitioning of your disk reduces the maximum size that it can have its filesystem on.
# Reset To Its Original Size (Windows)
1. `diskpart` to open diskpart utility
2. `list disk`
3. `select disk <disknum>`. select your usb drive
4. `list partition`
5. `select partition <partitionnum>`
6. `delete partition <partitionnum>`
	1. `delete partition override <partitionnum>` if its a protected partition
7. `create partition primary`
8. Close diskpart, and open `diskmgmt.msc`
9. Right click the disk and format. 
   ![[Restore USB Drive Space-20240708144218664.webp]]