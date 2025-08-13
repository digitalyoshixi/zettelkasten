---
tags:
  - cryptography
  - os
aliases:
  - TPM
---
![[Trusted Platform Module-20240525142022551.webp|377]]
A hardware platform for:
- Generating keys
- Storing keys
- Storing software signatures
Used for:
- [[Windows BitLocker]]
- [[Digital Rights Management|Hardware DRM]]
- Network access control
- Application blacklist
- Password protection
- Keygen
- Digitally signing data
- [[Hyper-V]]
- Preventing brute force by locking down [[File System]].
The TPM also has persistent memory so keys can be stored on the TPM.
The TPM is password protected.
# TPM Reset
After motherboard upgrade, reset the TPM so that it can access the data on your old disks.
