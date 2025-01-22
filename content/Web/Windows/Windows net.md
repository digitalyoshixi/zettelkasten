---
tags:
  - windows
aliases:
  - net
---
A myriad of tools for managing shared files on a network.
# net view
Command to see what shares are available and what computers are networked
### `net view`
See what shares there are
![[Windows net-20240718025335603.webp]]
The resulting computers are in [[Universal Naming Convention|UNC]] and can be accessed by typing their path in [[Windows File Explorer]]
### `net view <device>`
Will show all files and folders shared with them
![[Windows net-20240718025440529.webp]]
### `net view /workgroup:<workgroupname>`
# net use
To mount and use resources.
### `net use <drive>: \\<servername>\<sharename>`
![[Windows net-20240718025522408.webp]]
Will mount the `research` folder in server1 to the `x:\` directory
![[Windows net-20240825172459850.webp]]
# net user
View user account information and reset passwords
### `net user <username>`
View user information
![[Windows net-20240819195844564.webp|409]]
### `net user <username> * /domain`

### `net user <username> <password>`
To create users
` net user administrator SuperSecurePassword /active:yes`
# `net start <service>`
Starts a service.
`net start spooler` starts the printer spooler service
# `net stop <service>`
Stops service.
`net stop spooler` stops the printer spooler service
# Net Config Workstation
![[Windows net-20240718025820551.webp]]
Returns information about windows login
