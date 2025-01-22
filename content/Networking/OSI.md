---
tags:
  - networking
  - networking_model
aliases:
  - Open System Interconnections
---
One of the now derelict networking models. Replaced by the [[TCP & IP]] Model in prevalence. However, we still talk about the OSI because it was a damn good model. And fuck anybody who says it wasn't. It was perfect!

**The reason why we still talk about the OSI model is because of the terminology. People still use the terminology in regards of layers in terms of the OSI model.**

# OSI vs TCP/IP
as with TCP and IP, OSI is a layer model gathering protocols others have made and organizing them into corresponding layers.
![[Pasted image 20230924122221.png]]
We can map each layer in the TCP/IP model to  the layers in the OSI model. The only real difference it has to the TCP/IP model with the split link layer is that the application layer in the TCP/IP model is split into a Application, presentation and session layer in the OSI.

Claiming that one layer in TCP/IP is similar to a layer in the OSI is a general comparrison, not entirely wrong, but neglecting the means to the end. Sure, both transport layers exist to make sure packets are sent, but the methods OSI uses vs TCP/IP are much different. The goal is the same, the means to get there are different.
# The Layers
- [[OSI Application Layer]]
- [[OSI Presentation Layer]]
- [[OSI Session Layer]]
- [[OSI Transport Layer]]
- [[OSI Network Layer]]
- [[OSI Data Layer]]
- [[OSI Physical Layer]]

## Mneumonic phrases for memory
*"All People Seem To Need Data Processing"* (7-1)
https://www.cybrary.it/blog/osi-model-7-layers-basic-understanding 
PeDeN TSsPA
Peter Dinklidge Now Tries Scented Penis Antlions

## Layered Approach Benefits
The benefits of this layered approach means that each product for each layer does not have to worry about the other layers. Assume other software packages or hardware devices implement the functions for you.
This makes things several things better:
- **Less complex**. network models break things into layers
- **Standardized**. allows vendors to create products for a particular role
- **Easier to Learn**. better to discuss the details of protocol specifications
- **Easier to Develop**. reduced complexity allows easier program changes
- **Mutlivendor Interoperability**. Different vendor solutions often work with the same network
- **Modular Engineering**. one vendor can write softwar for higher layers, another can build the lower layers.

