---
tags:
  - networking
  - programming
---
The process of structuring several types of data into one packet/module.
# Networking
Transmission protocol used for creating [[Network Messages]]
**Encapsulation is the process of putting headers and trailers around payloads**

Encapsulation occurs in all layers, but the general term Encapsulation is really only used in the [[TCP & IP Network Layer|Network Layer]] and then [[TCP & IP Data Layer|Data Layer]] to distinguish between the different methods of Encapsulation those layers have.

For more information, consult each respective page:
- [[TCP & IP Network Layer|Network Layer]]
- [[TCP & IP Data Layer|Data Layer]]
# General Encapsulation from Application->Physical
For example, sending an HTTP request and getting an HTTP response will send data back with an:
- HTTP header with response code "OK"
- TCP header for current SEQ number
- IP header for the first packet.
- Data layer encapsulation in preparation for physical [[Bit Transmission]]
![[Pasted image 20230910170612.png]]
One step corresponds to the role of each layer.

## 5 Step Process
The process can be divided into 5 steps.
![[Pasted image 20230910170032.png]]
We use our 5 Layer model for this one.
1. **Create and encapsulate application data with application headers**. For HTTP, that is the HTTP header "OK(200)"
2. **Encapsulate data inside a TCP header**. Used to count the current packet sequence number
3. **Encapsulate data inside IP header**. To tell them what this address is
4. **Encapsulate data inside Data header and trailer**. Different depending on whether you are using the [[Point-to-Point Protocol]] or [[High-Level Data Link Control Protocol]]. An example encapsulation for PPP looks like this: ![[Pasted image 20230910171355.png]]
5. **Transmit the bits**. Physical layer encodes the data as a signal. 

