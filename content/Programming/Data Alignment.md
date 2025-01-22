---
tags:
  - math
  - memory
---
When computer reads/writes to memory addressess, it does it in chunks of 2,4,8,16,32,64 byte chunks. They are typically word size(4 bytes in 32bit systems) but can be larger  

What helps then, is that alignment of data matches the chunk size we read.

A problem with older hard drives that are not fragmented. It takes more time to get all bytes of file because it needs to physically move the read/write head depending on the bytesize.

If we can read the data in 4byte chunks, then we can load aligned.

So, this saves on CPU time reading/writing.

You may need to have padding to maintain that alignment. Certain C structures will include integers, chars, datatypes with different bytesizes. So typically when you malloc, you need to sum the members then pad to the nearest wordsize.

I may say that this padding is just garbage bytes. 00000000, 0x0, 0 something of the shit

  

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivev_tmp_be4de411fd827b77.png)

So the assembly code above is actually creating a pointer in ebp. Then the subtract will subtract the size of the local variable + padding (12 bytes)

what actually ebp is, is ebp holds a structure. The structure has:

1. A Short(2 bytes)
    
2. A pointer(4 bytes)
    
3. A Integer(4 bytes)

2+4+4 = 10.

the wordsize on the 32bit machine is 4 bytes.

So, the closest multiple to 10 would be 12. hence why we subtract 12 from the esp.
