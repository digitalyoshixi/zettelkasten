---
tags:
  - networking
  - networking
---
The TCP/IP model defines and references a large collection of protocols that allow computers to communicate through [[Network Messages]]

To define a protocol, the TCP/IP uses documents called RFC(Requests for Comments). You can actually view all of them, they are open for the world to see. This is a website to look them up: [https://www.rfc-editor.org/retrieve/](https://www.rfc-editor.org/retrieve/) RFC documents are protocols ok? They are very very specific as well. Like for example, this is one: [https://www.rfc-editor.org/info/rfc1558](https://www.rfc-editor.org/info/rfc1558)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw98_tmp_9c4a754d5016c7b5.png)

how people can use search filters inside LDAP access protocol to search directories. By simply following these protocols, the TCP/IP model avoids repeating work already done by standard bodies or vendor consortium in regard of definitions. For example: the (IEEE) Institure of Electical and Electronic Engineers defines Ethernet LANS, the TCP/IP does not define Ethernet in RFC, but refers to IEEE Ethernet as an option. Since this protocol is used for many devices, it is RFC that allows different devices to connect to the internet using relatively similar methods. A good comparrison can be made: you have a old broken phone connected to a telephone line RJ11 cable I think. You buy a new phone, hook it up to the same telephone cable, and the new phone works! Similarly, you buy a new computer, plug in a RJ45 cable in, and it works! No manual configuration, it just works! The OS on the computer implements part of the TCP/IP model. More specifically, the ethernet card hardware or wireless LAN card. So TCP/IP requires both hardware solution and hardware compatibility.

### Layers

To understand a network model, people often break it down into layers

TCP/IP has 2 models actually. One is the original, the other is the updated version which removes a layer and adds 2 more.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw9a_tmp_d9f45835cc6903dc.png)

the network access layer OR as some may call it, link layer, is replaced with the data link layer and physical layer.

The top 2 layers: Application and Transport focus primarily on how applications send and receive data. The bottom layer focuses on transmitting bits over each individual link, with the internet layer focusing on delivering data over the entire path of the internet. Navigating from our computer, to the computer somewhere else in the world.

The model on the right is more commonly used today, since it is the newest model.

There are many protocols that exist in different layers.

**[[TCP & IP Application Layer]]:** HTTP, POP3, SMTP

**[[TCP & IP Transport Layer]]:** TCP. UDP

**[[TCP & IP Network Layer]]:** IP

**[[TCP & IP Link Layer]]:** Ethernet, PPP(Point-to-Point Protocol), T1

Each layer provides a service to the layers above it. For example, HTTP wouldn’t be possible if you were linked via Ethernet or T1. TCP wouldn’t be able to transfer, had there not been a internet to begin with.

these layers may want to interact with different layers:
[[Same Layer Interaction]]
[[Adjacent Layer Interaction]]