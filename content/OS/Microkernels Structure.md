Like the monolithic structure, except instead of putting all functions in one kernel, we have microkernels. Most of the functionalities that would be in the kernel in a monolithic structure, have been changed into system programs. Microkernel provides communication between the system programs and the kernel, allowing for you to debug more specific things. Performance may be slower due to this approach.

Note: it is wise to run programs in user mode, because program errors in kernel mode will crash the entire system.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iv80_tmp_7379fb87770f19bf.png)

