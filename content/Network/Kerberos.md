---
tags:
  - networking
---
![[4575916404506624-1971567252.gif|427]]
Created by [[Massachusets Institute of Technology|MIT]].
A [[Single Sign On]] authentication protocol used while the user is logged in. Grants them tickets for the current session.
- Uses [[Symmetric Cryptography|Symmetric Encryption]].
- Ensures packets are encrypted for authentication.
- Protects against [[Man-In-The-Middle|MITM]] and [[Replay Attack]].
# Protocol
We want host $A$ to talk to file server $B$
1. Assumed shared key both [[Authentication Server]] and host knows (could be host's password in [[Windows Active Directory|AD]])
2. Request a ticket from kerberos server to get [[Ticket Granting Ticket|TGT]]
	1. Send a request to talk to [[Ticket Server|Ticket Granting Server]], pass in $n_{a}$
3. [[Key Distribution Center|KDC]] returns a message that is [[Cryptography|Encrypted]] with a session ticket $K_{as}$ containing:
	1. Shared symmetric key $K_{at}$
	2. $n_{a}$ random number to stop [[Replay Attack]]
	3. $T$ time
	4. $L$ lifespan
	5. id [[Ticket Server|TGS]]
4. [[Key Distribution Center|KDC]] returns the [[Ticket Granting Ticket|TGT]] containing:
	1. Shared symmtric key $K_{at}$
	2. id $A$
	3. $L$ lifespan
5. Host $A$ sends request to talk to fileserver $B$
	1. Host sends request encrypted with $K_{at}$:
		1. id $A$
		2. $T_{a}$ time
		3. id $B$
		4. $n_{a}$ random number to stop [[Replay Attack]]
	2. Host sends [[Ticket Granting Ticket|TGT]]
6. [[Ticket Server|TGS]] returns a new ticket to talk to the server $B$ encrypted with $K_{at}$ containing:
	1. $K_{ab}$ shared key
	2. $n_{a}$ random number
	3. $T_{t}$ time
	4. $L$ lifespan
	5. 
# Concepts
- [[Key Distribution Center]]
	- [[Authentication Server]]
	- [[Ticket Server]]
- [[Kerberoasting Attack]]
- [[Kerberos SSO Process]]
- [[Ticket Granting Ticket]]
- [[Updated Sequence Number|USN]]
- [[Mutual Authentication]]
- [[ntds]]