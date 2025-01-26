---
tags:
  - windows
  - networking
aliases: []
---
The [[IT/Windows]] version of [[traceroute]].
Tracks the route a packet goes from your machine to the destination machine.
Helps in troubleshooting bottleneck problems.
[[pathping]] is an alternative to tracert
# Command
`tracert <url or ip>`
![[tracert-20240717191336755.webp]]
# Process
Tracert abuses [[Time To Live|TTL]] error messages.
Several packets are sent out with increasing TTL hops. For the router that corresponds to the TTL hop, the router will respond with their IP address.
1. Send a TTL=1 packet
   ![[tracert-20240819201510339.webp]]
   ![[tracert-20240819201523061.webp]]
2. TTL Exceeded. Error message is sent back from the router. Within this error message includes the router's IP address.
   ![[tracert-20240819201556554.webp|411]]
3. Send TTL=2 packet and receive the IP of router 2
   ![[tracert-20240819201653311.webp]]
   ![[tracert-20240819201708357.webp]]
3. Continue sending increasing TTL packets until there are no more error messages.
   ![[tracert-20240819201823103.webp]]
   ![[tracert-20240819201836285.webp]]