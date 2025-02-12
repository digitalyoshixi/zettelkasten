---
tags:
  - windows
---
*Note: Mapped drives will retain [[NTFS Permissions]] and may prevent access if the share is moved in location*
# File Explorer
1. [[Windows File Explorer]]
2. Right click 'This PC' and click 'Map network drive'
   ![[Windows Map Network Drive-20240718022042040.webp|530]]
3. Select the folder you want to be shared
   ![[Windows Map Network Drive-20240718022215260.webp|439]]
# [[Windows net|net]]
`net use <driveletter>: "\\<servername>\<sharename>"`