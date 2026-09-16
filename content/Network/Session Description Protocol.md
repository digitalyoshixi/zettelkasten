---
tags:
  - networking
aliases:
  - SDP
---
A package of information shared between two devices that is used as part of [[WebRTC]].
Used to find your peer across the internet
![[Session Description Protocol-20260916155527758.webp]]
# SDP Object
![[Session Description Protocol-20260315015853718.webp]]
Contains:
- Version `v=0`
- Originator details (session id, sesion version number, IP address)
- Session duration `t=*`
- Audio or media streams `m=*`
	- `m=stream_type placeholder PROTOCOLS stream_id`
	- `m=audio 9 UDP/TLS/RTP/SAVPF 111`
	- `m=video 9 UDP/TLS/RTP/SAVPF 96`
- Attributes
	- Mapping audio/media to [[Video Files|Codec]]:
		- `a=rtpmap:111 opus/48000/2`
		- `a=rtpmap:96 VP8/90000`
	- [[Interactive Connectivity Establishment|ICE]] credentials
		- `a=ice-ufrag:myuser`
		- `a=ice-pwd:mypassword`
	- Fingerprint for [[Datagram Transport Layer Security|DTLS]] negotiation
		- `a=fingerprint:sha-256 4A:AD:B9:...`
	- Duplex type
		- `a=sendrecv`
		- `a=send`
		- `a=recv`
		- `a=inactive`
