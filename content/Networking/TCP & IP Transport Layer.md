---
tags:
  - networking
aliases:
  - Transport Layer
---
There are marginally fewer protocols that exist within the transport layer. The 2 more common ones are the TCP(Transmission Control Protocol) and the UDP(User Datagram Protocol).

Transport layer protocols provide services to the application layer protocols during packet transfer. More specifically, TCP has their own set of documents that handle error-recovery.

In our example above with the HTTP request for a web server, if any of our request or response packet was lost, say maybe the network is too congested, or wire troubles, our packets would be lost, and as a result, we wouldn’t be able to send our request, or receive our webpage.

Lucky for us, TCP has a mechanism to guarantee data delivery across the network. It uses the concept of adknowledgement.

Each response packet has their own SEQ(Sequence number). So, if for example, our response went like this:

**Webserver: SEQ 1| OK(200), [webpagedata]**

**Webserver: SEQ 2| [webpagedata] → lost!!! this packet is lost!!!**

**Webserver: SEQ 3| [webpagedata]**

**Our computer: Send SEQ 2 next.**

**Webserver: SEQ 2| [webpagedata]**

  

So, our computer noticed that SEQ 2 was lost, since it sent SEQ 1 and SEQ 3, but not SEQ 2. The realization leads our computer to sends a http request for the webserver to send packet 2 again.