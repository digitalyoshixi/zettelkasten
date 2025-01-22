---
tags:
  - Lena
  - reverse_engineering
---

### Sizes

1 byte == 8 bits == 2 hex digits == max of 255 == 1 opcode

2 bytes == 1 word

4 bytes == 2 word(dword)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd0_tmp_883f97bbabad2f9f.png)

Registers hold 4 bytes/32bit. The 16bit and 8bit counterparts may not be addressed directly

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd0_tmp_eea3b21e69e693e.png)

[[OllyDBG]] can control the program, we can control olly. Controlling the program ourselves is too much work. Ollydbg is a debugger so we can create breakpoints and step ins


### Test buttons

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd0_tmp_e68de66cdf4804ce.png)

From left to right:

Folder: Open a new file

Reverse: Restart the program

X: Terminate program

Play: Run the program all the way until end

Pause: Only when during run, you can pause then do steps

Step into: enter functions

Step over: execute function call once

The following, I have no actual idea. These are all guesses

Trace into:

Trace over:

Step break: run until next breakpoint

Make breakpoint: doesn't really work tho

  

### Calls

You can call in 5 ways. Pretty sure this also applies to jumps

1. Call label. Jumps to label
    
2. Call address. Call 40400000 will jump to 40400000
    
3. Call register. Call eax will jump to the value inside eax.
    
4. Call dword. Call dword ptr [eax+5] will go to the value at address eax+5. If eax was like 1, then it would go to address 6.
    
5. Call \<jmp to API\> executes an api function. Check the specific api for what it does.
    

The win32 api is usually stored in dll files. Win32 api allows for elevated permissions(lower ring level) actions. You must also give it arguments for every api call.

  

### mov 

Mov dest, src

There are some variations like movs, mov sx, movsb which alter the bitsize and esi or edi.

  

The confusing ones will be like:

Mov dword ptr ds:[402177], eax

This means we move the value in eax into memory address 402177

### Comment section

This is incredibly helpful, especially when its manually written. It helps you make sense of the mnemonics in an even clearer setting. Each comment corresponds to the line beside it

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd4_tmp_373062bee6f2bbee.png)


### [[Win32 API]] help

Depreciated. In our case, we cannot consult for help using windows help feature. Windows 8 was the last version in which this was supported. [Error opening Help in Windows-based programs: "Feature not included" or "Help not supported" - Microsoft Support](https://support.microsoft.com/en-us/topic/error-opening-help-in-windows-based-programs-feature-not-included-or-help-not-supported-3c841463-d67c-6062-0ee7-1a149da3973b)

Used to be so good too. Told you what parameters for each function.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd4_tmp_fe95e06531632c01.png)

What we have in its place is a more difficult to navigate webpage with mostly the same information. There is a charm, y'know, to old dos and xp graphics. A bit of ugly graphic design goes a long way to keeping the reader engaged. Anyhow, here it is: [https://learn.microsoft.com/en-us/windows/win32/api/](https://learn.microsoft.com/en-us/windows/win32/api/)

## Decimal from signed 2s complement

You might have seen this when doing a rapidtables calculation:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd4_tmp_e516a45eabc5442d.png)

FFFFFFFF, the largest 32bit number is also -1???

What does the decimal from signed 2’s complement mean?

Well, what we know is that it allows for negative numbers. And it all depends on the first digit.

From 0-7, all numbers are positive

From 8-F, all numbers will be negative

This makes quite a bit of sense when you realize that in binary, 7 is 0111 and 8 is 1000. And so on for 8 and above to F, the leftmost digit remains 1. We get the sign from the leftmost digit. 0 for positive, 1 for negative

  

So, why isnt -1 the just 4294967295 but negative?

And not only that, but the higher the negative hex, the smaller the decimal is? F0000000 = -268435456 but FFFFFFFF = -1.

The reason is that, the logic changes once we reach 8 as the first digit.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd4_tmp_2c0863a80af59844.png) [https://www.youtube.com/watch?v=RbJV-g9Lob8](https://www.youtube.com/watch?v=RbJV-g9Lob8)

What the image above means is that if the number is negative(1 in the leftmost digit), then the decimal value is: Hex - largest value possible

For 32bit, this largest possible value is 16^8 = 4294967296. For FFFFFFFF in this example, FFFFFFFF = 4294967295. So, 4294967295 - 4294967296 = -1. Checks out right?

  

The logic for positive numbers doesn't really work out, but we already know how to get positive numbers anyways. Just regular hexadecimals.

  

So therefore, the largest negative number will be 80000000

### Crack #1

We are set up with a program in ollydbg that is a gatekeeper to free software(dubious in content). It asks for a valid license.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_1987419e7c56ea8e.png)

Grr, how could you! Don’t you know? Open source open doors!

Lets enact our revenge.

  

# First skill - Flag manipulation

The first skill we learn is to look at where the error message is located in memory.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_4d8200fd6ff1cd63.png)

We are reading the comments here. Some condition is forcing a jump towards the event that says “BAD BOY DETECTED. NO LICENSE FIEND!” and then exit the program.

If we loop up, we find that this is occurring because of a comparison that changes the zero flag.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_63e4faf40fd48120.png)

The jnz will save us, but unfortunately we don't fulfill the conditions if we run it regularly to reach the jnz.

This means that after the comparison of eax and -1, the zero flag is ticked. Why is eax = -1?

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_fa31d55b0edb87f9.png)

Looking above, we find our answer. CALL <JMP & KERNEL32, CREATEFILEA> changes eax to -1 after completion.

[https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilea](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilea)

­CreateFileA is a winapi command. Lena tells us that it specifically looks for a filename. The filename in this case, is “Keyfile.dat”

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_2191ac0954cbdbf8.png)

We can assume then, that because we dont have this file “Keyfile.dat”, eax is turned to -1, thus causing our bad boy termination

So lets do this. Lets change the zero flag to false(0), then we can get to the jnz address and continue like we are legitimate customers.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_d1e0be6c3b6387f6.png)

And hey, it worked! We are now at 0001109A.

But we haven’t hit it home yet. Theres still one last struggle we must overcome.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_63ca0e7333b709c6.png)

And that is, read file. [https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-readfile](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-readfile)

It asks for data in memory addresses that would have been altered during the CreateFileA function, but we skipped that.

The sad thing here is that we still don't have “Keyfile.dat”!!!! So, are we fucked?

Wallow in misery, or retaliate against the proprietors. Remember, everything program flow is decided by flags and jumps.

  

Readfile will test eax. That weird ass test over here.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_c785fc34995c027f.png)

Test eax, eax. This will AND eax with itself. Literally changes nothing, BUT it does flick the zero flag IF and only IF eax was 0 before.

What occurs after? A jnz yalrealy know.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_6a1d6e1b436ebb4d.png)

Here's the rundown of what ReadFile does:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_3b68c68f83e3b89.png)

Readfile was going to read 0x46 at memory address 402173. Because it didn’t find it, eax is now 0.

So let's see the jumps. The JNZ is what we want to get to, the JMP probably leads to a bad place.

  

Indeed it does. The JMP to 004010F7 goes to write the bad boy message.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_ff4a041e15228e4d.png)

  

So we flick the zero flag after the test, get to the JNZ we want and then what happens?

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_4fbc754134e3cd2a.png)

IT LEADS TO THE BADBOY MESSAGE STILL!!!!

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_460fed218b89aff9.png)

FUCK IT WE LOOK AT STRINGS.

  

# Second skill - Referenced strings and backtracking

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_f0b31c00b289a910.png)

Referenced strings tab is pivotal. We dont want to search through heaps and tons of memory jungle to find all the badboys. So we’d read from here to view all referenced strings.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_707edd66c830084a.png)

So let's go to the good boy message we found.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_c570f23c03ae37d1.png)

Right, we found it, but we also need to find what jumps to this memory location.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_7f19721b5cc13c30.png)

Click the memory address with the arrow. You can see where it jumped from, you could also just follow the red line beside the memory address upwards.

  

We… are very close to where we were before.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_74b97133218926d2.png)

Ok, well atleast we know we are on the right track.

We need to get to the JMP to 00011205. To do that from where we are in the program now, we need to analyze each of the conditional jumps below us and their memory jump location. Find the closest one that will lead cohesively to 000110D8(our jmp to the goodboy)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_b0ede72503195a6d.png)

So, it looks like the JE on memory address 000110C9 will bring us closest to the goodboy jump, so we know we need to fufill that condition. The road to get there will be as follows:

1. Fail the JL jump on memory location 000110BF
    
2. Complete the JE jump to 000110D3
    
3. Fail the JL jump on memory location 000110D6
    
4. Complete the goodboy jump
    

How do we pass the JL jumps? Well the JL jump requires the S flag(sign) to be ticked on(1). Because we subtract and check if we got negative which means it's smaller. So whenever we are on the jump pad, we must make sure that the S flag is 0.

How do we fuffil the JE flag? Retard, do i even need to tell you this? JE = JZ = Zero flag == 1

  

Alright, once we have made it here just enjoy the ride. Press this button to continue

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_c1b4e1728640da12.png)

  

# Third skill - Patching

Right, now if you did this manually, you would have to change each flag during each jump, and that is quite the headache. We can’t always be there to guide olly so lets make a patch.

You know all the conditionals like JNE, JL and stuff? If we need those to jump, then why not change those to just JMP?

We can do this by double clicking the opcodes and writing whatever JMP instead

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_f5c5aec9deb47b3d.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_3b63cd2a0fa7fded.png)

This process is called assembling. We are rewriting the assembly code.

Let's rewrite all the conditionals that we need.

1. The jnz after createfile
    
2. The jnz after readfile
    
3. The je before the goodboy(actually not really cuz it automatically is the same)
    

Note: we could also just change a jump to jump directly to the goodboy memory location. This would save a lot of time, but it may miss crucial memory modifications along the way.

  

If we follow the cohesive way, you may also remember that there are jumps we want to avoid.

1. The jl after readfile
    
2. The jl after the je
    

To avoid these, just turn them into junk instructions. The easiest way is to change them to operand NOP. This just adds 0 to eax.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_143c73b42e3dee42.png)

Also check the box that says Fill with NOP’s. This will NOP the stragglers left behind that depend on that operand changed

  

DONT RUN YET! BEFORE YOU RUN! SAVE THE PATCHES

  

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_1b9eb1a6c41d4f89.png)

2. Select your modifications
    
3. Copy to executable. Both options are the same
    

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivd9_tmp_55025d348c94fc86.png)

There we go, go ahead and run the exe and see the goodboy message. Good boy!