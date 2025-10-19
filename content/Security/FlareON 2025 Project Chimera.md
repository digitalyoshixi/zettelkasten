---
tags:
  - reverse_engineering
---
# Soln
We have the current file:
![[FlareON 2025 Project Chimera-20251017235115625.webp]]
Dump the bytecode in a pyc [[Create pyc from Bytecode]]
Then, decompile the pyc in [[Pylingual]].
![[FlareON 2025 Project Chimera-20251017235156548.webp]]
Then, lets dump this bytecode again...
![[FlareON 2025 Project Chimera-20251017235257447.webp]]
Ok, now that I know this isn't malware, lets try running it.
Ok, so after running we directly get this status:
![[FlareON 2025 Project Chimera-20251017235657354.webp]]
Now, what its checking is for the current user.
![[FlareON 2025 Project Chimera-20251017235810732.webp]]
![[FlareON 2025 Project Chimera-20251017235914248.webp]]
Our goal is now to find the current_user. We do this by reversing the user_signature. Which we know must be equal to LEAD_RESEARCHER_SIGNATURE.
The reversing script is such:
```python
LEAD_RESEARCHER_SIGNATURE = b'm\x1b@I\x1dAoe@\x07ZF[BL\rN\n\x0cS'
i = 0
endstr = []
for byte in LEAD_RESEARCHER_SIGNATURE:
	endstr.append( chr(byte ^ i + 42) )
	i+=1
print("".join(endstr))
```
![[FlareON 2025 Project Chimera-20251018000503680.webp]]
Ok, now we know the key.
Lets write the final decryption script:
```python
from arc4 import ARC4

import cowsay

current_user = "G0ld3n_Tr4nsmut4t10n".encode()
ENCRYPTED_CHIMERA_FORMULA = b'r2b-\r\x9e\xf2\x1fp\x185\x82\xcf\xfc\x90\x14\xf1O\xad#]\xf3\xe2\xc0L\xd0\xc1e\x0c\xea\xec\xae\x11b\xa7\x8c\xaa!\xa1\x9d\xc2\x90'
arc4_decipher = ARC4(current_user)
decrypted_formula = arc4_decipher.decrypt(ENCRYPTED_CHIMERA_FORMULA).decode()
cowsay.cow('I am alive! The secret formula is:\n' + decrypted_formula)
```

![[FlareON 2025 Project Chimera-20251018000811646.webp]]