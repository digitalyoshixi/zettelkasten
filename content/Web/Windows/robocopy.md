---
tags:
  - windows
---
Robust file copy. Better version of [[xcopy]]
Enables copying files or folders across networks
`robocopy sourcedir remotedir /mir`
The `/mir` flag will copy everything from the source and make the destination mirror to it.
Robocopy will delete anything in the destination that doesn't match the source