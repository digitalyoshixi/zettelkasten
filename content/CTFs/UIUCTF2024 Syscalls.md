---
tags:
  - ctf
  - binary_exploitation
---
# Challenge Resources
![[UIUCTF2024 Syscalls-20240630223119347.webp]]
### Download Links
https://uiuctf-2024-rctf-challenge-uploads.storage.googleapis.com/uploads/849d00c7cde64633f69d88a2089d86cb207d28fe05c3eb92bec9013356ec0d85/syscalls
https://uiuctf-2024-rctf-challenge-uploads.storage.googleapis.com/uploads/bd29ee29287ad1a656065cc4f4d26093fe3f952c8e6a2e286ff8ad22d079ccdd/Dockerfile
### Initial Recon
Connecting to the netcat server, we see that the flag is located in `flag.txt`
![[UIUCTF2024 Syscalls-20240701050011458.webp]]
# Solution
https://flex0geek.blogspot.com/2024/07/pwn-writeup-syscalls-and-backup-power.html#2
This is of course, a jail challenge.
Using seccomp tools to find the forbidden syscalls:
![[UIUCTF2024 Syscalls-20240701164347937.webp]]
Then, when we load the binary into ghidra to reverse it, we see that its just a simple, take user input, then execute it provided the user input does not have any forbidden syscalls.
![[UIUCTF2024 Syscalls-20240701165206102.webp]]
A list of syscalls can be found here:
https://x64.syscall.sh/
This was the C code to exploit the syscalls openat, preadv2, pwritev2:
![[UIUCTF2024 Syscalls-20240701170832859.webp]]
And then they sent the assembly to do the same
![[UIUCTF2024 Syscalls-20240701170908353.webp]]