---
tags:
  - windows
---
A tool to manually partition drives or clean drives.
# Clean Drive
1. `list disk` to find the disk your want to clean
2. `sel disk <disknum>`
3. `clean`
4. go into [[Windows Disk Management|diskmgt.msc]] and format the drive to be FAT32
# See Volumes
`list volume`

# Diskpart Access Denied
1. `convert gpt`
2. `clean`
3. then use [[Windows Disk Management|diskmgt.msc]] to create the simple volume