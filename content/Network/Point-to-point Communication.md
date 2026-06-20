---
tags:
  - networking
aliases:
  - Half Duplex
  - Full Duplex
  - Simplex
  - Duplex
---
In Point-point connections, data sent can either go one way (Simplex) or both ways (Duplex).
- There is no requirement for addressing (as you already know the guy on the other end)
# Simplex
![[Point-to-point Communication-20240716180246237.webp]]
There is only one-way that data can go
# Half Duplex
![[Point-to-point Communication-20240716180259072.webp]]
Data can go either way, but there is only 1 stream so transmitting and receiving must take turns.
Half duplex follows [[Carrier Sense Multiple Access|CSMA/CD]] as its communication protocol.
# Full Duplex
![[Point-to-point Communication-20240716180324356.webp]]
There are designated transmitter and receiver endpoints. Data can be transmit and received at the same time.