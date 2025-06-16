---
tags:
  - ctf
---
# Info
![[SmileyCTF2025 Easy Come Easy Go-20250615001546411.webp]]
https://storage.googleapis.com/sctf-attachments/rev-easycome-easygo/easycome-easygo.tar.gz?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=registry-deployer%40eternal-respect-454600-c7.iam.gserviceaccount.com%2F20250614%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20250614T211914Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=57b8259ff1f7b7687bc768a8bf7f8de4814910b3c78e5255d8e33d24174f821a02fcb9cf873109b38189461fd0c8c222023540bbb1df3ceb06e1b9c211620ee32a79e481ad0c0684e8848aead179e634e1fa58aa7de121ea57e76d08724483ae606b01d618066ed926479c5656bb5869611ba561885aa5c2c59a3920f73c634b72424a5863f317021855c2708b55c7cfa36472d2e866632f38fcc2b8e21a8111eab3acd507b05718cfc3ef84e51008535dc476e77c5875307687dccb13373bec9b677d53dc3156f54a1b0218484d39c29914dc29ab39027c91883f38a6918f1f3fe0a27ee7f447af6a5e0967f1eb759f678d3cbc59f6b1349b2ee1f1a314e385
# Solution
The entry for go programs is `main.main`. In binary ninja, we get this for main:
![[SmileyCTF2025 Easy Come Easy Go-20250615002450883.webp]]
This first block, will check if there is enough RAM to load the program. If so, then we go to the right-block.
The right block will initialize [[Go Channels]], five of them, aswell as print a `> ` and ask for user input with scanf.
![[SmileyCTF2025 Easy Come Easy Go-20250615002714367.webp]]
Then, a simple flag length check is done before progressing forwards
![[SmileyCTF2025 Easy Come Easy Go-20250615002751512.webp]]
Then, a series of [[Goroutine|Goroutines]] are called. A goroutine will have this structure of checking write barriers before every call.
![[SmileyCTF2025 Easy Come Easy Go-20250615003302835.webp]]
At the very end, rbx recieves data from a channel, which is then compared to be equal to 0. If they are equal, then we get the winner flag.
So, in essence, the very last goroutine we call which is `main.main.func3` will determine if we win or not. 
![[SmileyCTF2025 Easy Come Easy Go-20250615003430178.webp]]
Again, there is the check for sufficient RAM for the stack, we can just ignore that.
Notice that there is a series of assignments to the stack. 24 in fact, perfect with the length of our flag. Lets call this list `f3list`
![[SmileyCTF2025 Easy Come Easy Go-20250615003525971.webp]]
The following loop will check iterate through all characters from 1-24 and do the following:
1. Get the current number from `f3list[counter]`
2. Send this to a channel that func1 listens to, and recieve the output
3. XOR that output with `ourinput[counter]`, and send this to a channel that func2 listens to, and recieve that output
4. Check that output with a hardcoded output
If this loop passes 24 times, then we win.

I used [[Delve]] to actually see which function was listening to which channel, since [[GDB]] had issues with concurrency.
![[SmileyCTF2025 Easy Come Easy Go-20250615004105756.webp]]
# Final Script
```python
firstecx = [0xcc, 0x02, 0x84,0xf2,0x1a, 0x42, 0xb1, 0x3e, 0x82, 0x5d, 0x30, 0x44, 0x12, 0x51, 0x6c, 0x6f, 0x2d, 0x4c, 0x51, 0xc1, 0x57, 0x47, 0xf,0xac]
lastecx = [0x5c, 0xef, 0x33, 0xd, 0x92, 0xd6, 0xc4, 0x58, 0xac, 0x23, 0x19, 0xf6, 0x76, 0x4, 0x25, 0x77, 0xd0, 0xdb, 0x1f, 0x90, 0x93, 0x3c, 0x90,0xf5]
func2 = [0xbe, 0xd6, 0x9b, 0xc4, 0xa6, 0xef, 0x12, 0x09, 0x46, 0x4d,0x44,0x83,0x05,0x3b,0x16,0x6a,0x95,0xa3,0x3e,0x64,0xf4,0x1f,0xe6,0x24]

listlen = len(firstecx)

for i in range(listlen):
    print(chr(firstecx[i] ^ func2[i] ^ lastecx[i]),end="")

for i in range(24-listlen):
    print("a",end="")
print("")
```