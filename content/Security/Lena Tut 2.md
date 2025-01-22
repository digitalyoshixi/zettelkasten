---
tags:
  - Lena
  - reverse_engineering
---
### The bits and the bytes

Why are there 8 bits in a byte? Well it's just something that people settled on over the past 80 years. The bytesize of 8 allows us to display all characters in the ascii alphabet

  

Win32 CHM/Help file

[https://sourceforge.net/projects/win32-help-chm/](https://sourceforge.net/projects/win32-help-chm/)

Yess, finally a working help file we can use offline. Good to be old

  

### Crack # 1

Same program as before. We need to activate a license

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ive0_tmp_1987419e7c56ea8e.png)

  

# Fourth skill - Strawman

Right, so remember the program has this readfile section.

### ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ive0_tmp_4bc5bf489dd48cee.png)

That reads for Keyfile.dat in the same directory

So let's create this Keyfile.dat file

  

Ok. so that check was successful. We encounter another impasse at the readfile call

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ive0_tmp_2a439db9052af965.png)

Later on, the 402173 address(our Keyfile.dat text) is compared to 16

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ive0_tmp_f1ad02d0a1b8754d.png)

The following JL leads us to the badboy message, so we know that 402173(our Keyfile.dat text) must be atleast 16bytes.

If our file has atleast 16 bytes, then we will reach this mov operation

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ive0_tmp_14041d6e13bb5e64.png)

EBX is a counter actually. Starts from 0 but you see it gets incremented later on. We now know that this is a loop.

AL initially becomes the first character of our Keyfile.dat text. But when EBX keeps incrementing, AL will eventually become all other characters too.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ive0_tmp_c024c4d27c0f2c1.png)

It later compares the AL with 0. This is actually checking if for null values. When this is true, then we stop.

So that JE is the ending. What happens at the end? We check ESI which is a general purpose register. As long as it's over 8, we jump to goodboy. Its zero at the beginning of the loop and it changes during the loop so let's see that

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ive0_tmp_7468516dae7ca3e1.png)

The logical progression is to ignore the JE which leads to the end of the loop. Since we are not end-worthy, we will compare al with 47h(0x47). We write in ascii so what is 47h in ascii?

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ive0_tmp_65fe145169d608f7.png)

G!!!! MY G!!!!

  

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ive0_tmp_a7bf9fffd61fdfc0.png)

If its not zero, we will jump to 004010D0. This means we DONT increment ESI, not helping the goodboy condition, we simply go to the next character in the loop.

If it is zero/equal, then we increment ESI and that's the only difference compared to the aforementioned condition. ESI helps in the goal of the goodboy

And thats the gist of the loop. Lets reinstate the conditions:

1. Must have atleast 16 bytes( in our case ascii characters)
    
2. Atleast 8 of those characters are 8
    

Right, so an example valid key would be: G0G0G0G0G0G0G0G0

Another can be: G11111111GGGGGGG

Even moreso: GUCKINGRAGGGGGG

Godamn what a horrible key to have. How easy to crack!

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ive0_tmp_e6dfc3edbd7793cc.png)