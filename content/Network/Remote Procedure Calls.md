---
tags:
  - networking
aliases:
  - RPC
---
Protocol one program uses to request services from another program on a network WITHOUT knowing the network’s details. 


Similar to an [[Interprocess Communication]], but we must use message based communication as processes are executing on separate systems.

The messages being sent on the networks are more advanced than the ones sent through IPC. Each message is sent to a RPC daemon(background process) listening to a port on the remote system. The message contains function identifier and parameters to pass that is then executed and sends the output back to the original sender.

Remote host receives the message with help of a stub. This stub helps in locating ports, receiving parameters, marshaling(organizing).

Marshaling involves packaging parameters into a form that can be transmitted over networks

Your local device also has a stub that receives this form and does the same.

If needed, successful transfers may also output a return code for the sending machine

###   

### RPC issues

Because we are using 2 computers, conflicts may occur due to firmware or software limitations
 
| Issue                                                                                                                                                                                                                                | How it is resolved                                                                                                                                                                                                                                                                                                                                                                                                                                               |     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| Difference in data representation. 32 bit integers are stored differently. Big-endian systems store the most significant byte in high memory address. little-endian systems store least significant byte in the high memory address. | RPC uses a special format to manage data. An example format is external data representation(XDR).                                                                                                                                                                                                                                                                                                                                                                |     |
| RPC can fail, duplicate or execute more than once due to network errors.                                                                                                                                                             | Os ensures messages are sent exactly once.                                                                                                                                                                                                                                                                                                                                                                                                                       |     |
| Procedure calls on a local computer will bind 2 programs. This must require knowledge of other ports. Client does not know because they do not share memory.                                                                         | 1. Agree on fixed port numbers. During compile time, RPC assigns a port number to our client. We cannot change this port unless service is completed.<br>    <br>2. Dynamically figuring out ports. An OS provides a rendezvous/matchmaker daemon on a RPC port. The rendezvous mechanism is where several receivers can find each other.<br>    <br><br>![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iv8t_tmp_3ba1931451160d43.png) |     |
|                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |     |
 
