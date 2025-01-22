---
tags:
  - Lena
  - reverse_engineering
---
We are given [[Nagware]] that nags us to purchase software with popups.

The nature of nagware will check for registration keys at program startup, meaning that if we find what the specific condition of this is, then we can effectively register without paying.

Our challenge is to not use referenced strings.

  

Note: This tutorial reverseme has been flagged as malware. Trojan of sorts

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iveb_tmp_fca2fe81031edef1.png)


### Crack It myself

Im going to try and use my current skills to crack this software.

- we dont know what the end product will look like

- there are 3 messages in the unpatched version

- Remove the nags to register This will make the program fully registered :))

- You need to register me now! It is supposed to be quite easy. Just patch the program to remove the Nags

- Oops! I am not registered !!

- the first message I dont think i can skip, but the second and third i can probably remove

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iveb_tmp_3c9bafcbbbb00447.png)

Search referenced strings and then go here.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iveb_tmp_e1c9f310f9003240.png)

This is the address of where the found string is located

The call GetModuleHandleA does nothing of importance. Just get the filename ReverseMe and store that in eax. Of course, since it exists, we bypass the je that would lead us to a bad scenario.

So actually, I realize this. The program has a register good message, but we never have the option to jump to it because there is no jump directly to it. Im going to try to patch and create a jump to it then!

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iveb_tmp_86ce6be099b1f07e.png)

And so apparently there is this entry point comment here for some reason. I will just jump to there. So replace the first line of code with a jump then

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iveb_tmp_4d288eceb0b70188.png)

Used to be push 0, now it is JMP 00401066

  

Yea so i did that, didn't do anything at all so I think I was led astray. Back to the lab again.

  

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iveb_tmp_eb0bdfec04f3ea4e.png)

What I did notice is that there is this args. Lets see what it compares them to…

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iveb_tmp_b3d67b3fe9acb5d8.png)

Yes so the call jumps here. There is sooo much information and loops and conditional jumps here. This is where we must go.


### Crack # 2
Right, so uhh I am just going to uhh follow the tutorial as it is yea?
Lena mentions something about text strings being obfuscated from methods like packing or encryption. Im thinking of making a crackme for cs club so these might be techniques to consider

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivej_tmp_f58cb6ba7a08fc4c.png)

So, yes, we want to fulfill the JE in order to move pass the badboy. The code below is the badboy because there, it is generating the evil message box!

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivej_tmp_92ab469535bf5e76.png)

Then we go to this segment. Message box not created.

Problem is, we keep going down and there are even more nags!

  

We are going to change entry points
### PE Locating

We are going to utilize the PE header from imagebase address. To crack this program

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivf1_tmp_f0dd0b5fbf807f52.png)

In our case, address 00400000 is the imagebase

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivf1_tmp_811bd9899cd8bc3d.png)

at 00400000, that is actually the MZ section which contains lastpage size, total pages in file, relocation items, etc as well as a pointer to the location of the PE header.

  

  

Alternatively, you can open this Memory map button:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivf1_tmp_1607844d6f3c0e0a.png)

Which will open this screen:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivf1_tmp_40f4159e6884985c.png)

Aheyyoooo, PE header right there!

Double click that address, it opens up

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivf1_tmp_5a4aad0e4f41f716.png)

And we also found the PE offset to tell us where the PE header is located

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivf1_tmp_a9430cb6a818903a.png)

Great, it tells us it is at an offset of 0C0, so we will need to go to 004000C0

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivf1_tmp_880c78091b9d022.png)

Indeed it is

  

To clear up some inconsistencies, using the first method with the hex dump, we see that the PE header location is actually ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivf1_tmp_e74e0bc4fc6b4bb5.png)

C0 00 00 00

But using the second method of memory map, we see the PE header location is

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivf1_tmp_880c78091b9d022.png)

004000C0.

These are actually the same address. There are 2 reasons why

1. The hex dump sorts via little endian. C0000000 is the same as 000000C0 in big endian.
    
2. The hex dump starts reading from the image base(00400000) so it doesn’t include the 400000. It literally becomes a virtual address (relative virtual address)
    

### Relative Virtual Address

A relative virtual address is a virtual address used if you don’t know the exact memory locaiton you are referencing. It is an value you need to add(offset) from the imagebase of the PE file hence the relative in the name.

You can think of everything in the hex dump as a relative virtual address little endian form

  

We go to the section table section of the PE format. This lists all sections in relative virtual address form. Some sections may have a reference, some may not, some may point to the same section.

  

### Section Alignment

The PE header defines 2 alignment values for sections to use. One that points to the section on the raw disk, the other in memory(virtual address). From

the values the PE header gives, the actual section’s alignment is an offset of this value(usually a multiple of the value).

### Sections

Usually starting at RVA 1000 from the image base, sections start to appear

The section table is just an array that describes the location and size a section takes up. Allowing the loader to find a section very quickly. It is an array of IMAGE_NUMBER_OF_DIRECTORY(16 space reserved for entries) and IMAGE_DATA_DIRECTORYIES

  

The code section (.text) is the first one.

  

### PE linkage

When you use code or data from a DLL file, you are linking it. when you link against, the compiler will grab compiled code from the DLL and make them available in your code.

when any pe file loads. job of win32 loader is to:

- locate all imported functions

- locate all imported data

- make addressess avaiable to file being loaded

within a PE file, theres an array of data structures, one per imported DLL. each of these structures gives the name of the

imported DLL and points the an array of function pointers known as the Import Address Table(IAT)

  

each imported API/function has its own reserved spot in the IAT where

address of imported function is loaded/written by the win32 loader

  

the following is very important:

once the module/library is loaded into RAM, the IAT contains the addresses invoked when calling imported APIs.

the IAT is where all imported API addresses are stored so every call goes to the same function pointer in IAT

This is how it goes:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_b58c16b3a87a32fb.png)

from the PE header, we change the entry point to the address after the badboy message generation.

  

# Fifth Skill – Hex Edit

First thing I need to do is change my header to 00400000 (start of file) in the hex dump

Look where I am now:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_3f66369601f17c8e.png)

00403068

So I need to go to 00400000

Rightclick > Go to > Expression OR CTRL+G

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_a1df40e4a4056cda.png)

type in 00400000 then follow it.

  

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_92167331dfb95791.png)

Thar we go!

This hex dump section here allows us to change the memory values

I go to address 004000E8 in the hex dump.(the one that is selected right now)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_30096b31daada69b.png)

Notice it is on the 9th column. The first column is 004000E0, so thats the way its ordered. Goes up to F(15).

  

Right click > Edit > Binary Edit OR CTRL+E

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_58e2696137c6fdcc.png)

Ok, so I wanted to change the entry point instead of 0D to 24 instead. That will skip the badboy generation message

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_a2d73ce485cdf616.png)

  

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_750c17c8c95221aa.png)

Now we save the changes.

I select the entire byte 24100000

  

  

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_b44cd6bb3e3ccee7.png)

Then Right click > Edit > Copy to Executable

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_2a81267e83eae39c.png)

Rightclick > Save File

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_49dcc52fb0f1839f.png)

Arite

  

What you will see when you execute is that, yes we do skip the first badboy, but the other 2 still show up.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_a39ac51e0bf5865.png) ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_f43898d9cca0c584.png)

  

# Sixth Skill - Eradication

We are going to get our hands dirty.

The specific badboy messages are being generated from the mnemonics so we will need to remove the mnemonics. NOP them, wipe them outbound

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_66e45dbb2ed6459e.png)

These specific 5 lines are all used in the creation of the 3rd badboy. Nuke them and the arguments because we don’t want stragglers left in the stack.

Rightclick > Edit > Fill With NOPs

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_182889e998cee1d3.png)

Then save the changes to executable, and we are good

  

### Crack # 3

There is another file bundled into this lesson. RegisterMe_Oops.exe the gimmick with this one is that it is packed/protected meaning that upon olly running it, the PE file is unreadable.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_a187a9aa1a664606.png)

wet dog shit

  

Lena’s olly stopped at a system breakpoint, my olly stopped at WinMain. I will change it to lena’s breakpoint.

This is how its done:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_815afefee63bfc25.png)

Options > Options OR Alt+O

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_307144141134346c.png)

Change it to system breakpoint

  

Ok now, lets go to the Memory map

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_80256eb089af03cb.png)

Diagnose the problem. Go to the PE header portion

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_b0a825bfe15a3d69.png)

Then lets go to the AddressEntryPoint field.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_86c8811ea9693f31.png)

Here it is

Dont forget, Address Entry Point is a relative virtual address, we still need the IMAGEBASE to find the actual address. Lucky us, the IMAGEBASE field is right beside this one.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_110f7427f9f7cf8a.png)

so Imagebase is 400000. entry point address is then 401000

Lets go to there

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_92f0aa1ec078061f.png)

Rightclick > Go To > Expression OR CTRL + G

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_650f8570e1e14c56.png)

continue on

  

The following is now antiquated in Ollydbg2, Ollydbg1 had this bug, but Ollydbg2 fixes this feature

We try and put a breakpoint at 00401000

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_2b9962157b0500c3.png)

Olly is confused 🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭

  

So why does this happened?

Lets look back at the memory dump

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_58c176e3e72a8c76.png)

The PE header eats the sections!

Some fields were changed in this program that mess Olly up. Nothing fatal was changed and it can run as a regular exe. As a result, Olly gets confused

The fields that were changed are as follows

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_90b0210e05380699.png)

RVAs are messed up

SizeOfCode = 400

SizeOfInitializedData = A00

BaseOfCode = 1000

BaseOfData = 2000

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_44c31e33d983386a.png)

NumberOfRvaAndSizes = 10

Export Table Address = 0

Export Table Size = 0

  

Ok lets make those changes

In the hex dump, Go To the address where this whole charade started. 004000DC(i went to 004000D4 to change memory map layout. You can just calculate if different offset)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_1a8c965d06707c29.png)

Select a whole bunch of hex, then binary edit them or CTRL + E

Once the Triage is complete, we are as well.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_cbf03760f0ff0300.png)

Look at that healthy window! Hex dump looking sharp, entry point high in the sky.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfk_tmp_c409d84f061846ae.png)