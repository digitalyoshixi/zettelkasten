---
tags:
  - networking
  - networking
---
As both computers use the same protocol, they both follow an agreed set of rules. When one layer on one computer wants to communcate with another same-level layer on a different computer, like HTTP on my computer to HTTP on a webserver, we call this same-layer interaction. The 2 layers will use headers to communicate what they want to do. Our example above, the webserver sends heading that it will send you lots of packets for the file home.htm. When we lost a packet that was sequence 2, our OWN computer sent a packet with a header telling the webserver: “Hey! I lost this packet! Please send again!”.