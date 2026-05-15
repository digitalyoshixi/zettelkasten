---
tags:
  - networking
---
You open a tty on another computer to a server.
You forward a port from that server to be visible on this computer.
# Opening web UIs 
Very niche case, but think about this:
You spawned a TTY of your server. You dont have any browser on the server. Yet, you install a software that requires a web UI.
### Example with [[Syncthing]]
https://superuser.com/questions/1397683/how-can-i-configure-syncthing-from-command-line-to-share-a-folder-with-another-c
```
ssh -L 8080:localhost:8384 your.host.name
```
Then you can access the remote web GUI from http://localhost:8080