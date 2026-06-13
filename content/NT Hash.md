---
tags:
  - windows
  - security
aliases:
  - NTLM Hash
---
A hash easy to crack stored in [[Security Accounts Manager]] hive or [[ntds|ntds.dit]] on [[Domain Controller]].
NTLM hashes are combinations of NT and LM hashes.
- The LM has will always be `aad3b...` representing empty string
# Structure
```fallback
[Username]
 |
 v
Bob:500:aad3b435b51404eeaad3b435b51404ee:58a478135a93ac3bf058a5ea0e8fdb7
     ^                 ^                               ^
     |                 |                               |
   [RID]               |                               |
        [ ---------- LM Hash* --------- ]              |
	                                    [ --------- NT Hash  --------- ]  
	    [ ------------------------ NTLM Hash ------------------------- ]
```