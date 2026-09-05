---
tags:
  - windows
  - win32api
---
### Prefixes

| Prefix | Meaning                                                                                                                                                                                                                          |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Alpc   | Advanced Local Procedure Calls                                                                                                                                                                                                   |
| Cc     | Common Cache                                                                                                                                                                                                                     |
| Cm     | Configuration manager                                                                                                                                                                                                            |
| Dbg    | Kernel debug support                                                                                                                                                                                                             |
| Dbgk   | Debugging Framework for user mode                                                                                                                                                                                                |
| Em     | Errata manager                                                                                                                                                                                                                   |
| Etw    | Event Tracing for Windows                                                                                                                                                                                                        |
| Ex     | Executive support routines                                                                                                                                                                                                       |
| FsRtl  | File System Runtime Library                                                                                                                                                                                                      |
| Hv     | Hive library                                                                                                                                                                                                                     |
| Hvl    | Hypervisor library                                                                                                                                                                                                               |
| Io     | I/O manager                                                                                                                                                                                                                      |
| Kd     | Kernel debugger                                                                                                                                                                                                                  |
| Ke     | Kernel                                                                                                                                                                                                                           |
| Kse    | Kernel Shim Engine                                                                                                                                                                                                               |
| Lsa    | Local Security Authority                                                                                                                                                                                                         |
| Mm     | Memory manager                                                                                                                                                                                                                   |
| Nt     | NT system services (accessible from user mode through system calls)                                                                                                                                                              |
| Ob     | Object manager                                                                                                                                                                                                                   |
| Pf     | Prefetcher                                                                                                                                                                                                                       |
| Po     | Power manager                                                                                                                                                                                                                    |
| PoFx   | Power framework                                                                                                                                                                                                                  |
| Pp     | PnP manager                                                                                                                                                                                                                      |
| Ppm    | Processor power manager                                                                                                                                                                                                          |
| Ps     | Process support                                                                                                                                                                                                                  |
| Rtl    | Run time library                                                                                                                                                                                                                 |
| Se     | Security Reference Monitor                                                                                                                                                                                                       |
| Sm     | Store Manager                                                                                                                                                                                                                    |
| Tm     | Transaction manager                                                                                                                                                                                                              |
| Ttm    | Terminal timeout manager                                                                                                                                                                                                         |
| Vf     | Driver Verifier                                                                                                                                                                                                                  |
| Vsl    | Virtual Secure Mode library                                                                                                                                                                                                      |
| Wdi    | Windows Diagnostic Infrastructure                                                                                                                                                                                                |
| Wfp    | Windows FingerPrint                                                                                                                                                                                                              |
| Whea   | Windows Hardware Error Architecture                                                                                                                                                                                              |
| Wmi    | Windows Management Instrumentation                                                                                                                                                                                               |
| Zw     | Mirror entry point for system services (beginning with Nt) that sets previous access mode to kernel, which eliminates parameter validation, because Nt system services validate parameters only if previous access mode is user. |

### Suffixes
If you have no suffixes, then windows does the compatibility for you.
Only use suffixes if you want specific functionality

| Suffix | Meaning                                                                                                                                                                                                                                                                                                               |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A      | (A) ANSI Functions<br>`CreateWindowA` Uses ANSI characters. This prevents it from using special characters.                                                                                                                                                                                                           |
| W      | (W) Wide/Unicode Functions<br>Unicode. So chars do not take exactly 1 byte. This is opposite to (A), these function can use special characters.                                                                                                                                                                       |
| Ex     | (Ex) Extended Control<br>Very overloaded versions of the original for added functionality.<br>`VirtualAllocEx` allocates virtual memory inside **the calling** process `VirtualAllocEx` allocates virtual memory inside **any** process.<br>Allows you alot of fine tweaking<br>![[Win32 API-20240413222457480.webp]] |


# Combinations
If a argument allows a combination of enums, then you are able to pass it like `ENUM1 | ENUM2`.
