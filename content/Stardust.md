---
tags:
  - security
aliases:
  - Modern Position Independent Implant
---
A [[C2 Implant]] template written to be customizable and [[Position Independent Executable|PIE]].
- Support for global variables
- Support for raw strings
- Support for compile-time hashing
# Design
Implant is built with following sections:
```
[   .text$A    ] aligns the stack, executes entrypoint, util function to get the base address, etc. 
[   .text$B    ] C entrypoint, implant prepation, communication, commands, evasion techniques, etc.
[   .rdata*    ] literal strings and data (maybe even configuration) 
[  page align  ] alignt page by 0x1000 so ".global" section is in its own page
[   .global    ] global variables
[   .text$E    ] code to get the rip of the end of implant
```
# Writing Payloads
```c
#define D_SEC( x )  __attribute__( ( section( ".text$" #x "" ) ) )
#define FUNC        D_SEC( B )

FUNC VOID Main(
    _In_ PVOID Param
) {
    STARDUST_INSTANCE

    PVOID Message = { 0 };

    //
    // resolve kernel32.dll related functions
    //
    if ( ( Instance()->Modules.Kernel32 = LdrModulePeb( H_MODULE_KERNEL32 ) ) ) {
        if ( ! ( Instance()->Win32.LoadLibraryW = LdrFunction( Instance()->Modules.Kernel32, HASH_STR( "LoadLibraryW" ) ) ) ) {
            return;
        }
    }

    //
    // resolve user32.dll related functions
    //
    if ( ( Instance()->Modules.User32 = Instance()->Win32.LoadLibraryW( L"User32" ) ) ) {
        if ( ! ( Instance()->Win32.MessageBoxW = LdrFunction( Instance()->Modules.User32, HASH_STR( "MessageBoxW" ) ) ) ) {
            return;
        }
    }

    Message = NtCurrentPeb()->ProcessParameters->ImagePathName.Buffer;

    //
    // pop da message
    //
    Instance()->Win32.MessageBoxW( NULL, Message, L"Stardust MessageBox", MB_OK );
}
```
# Global Instance Variable
```c
#define InstanceOffset()   ( U_PTR( & __Instance_offset ) )
#define InstancePtr()      ( ( PINSTANCE ) C_DEF( C_PTR( U_PTR( StRipStart() ) + InstanceOffset() ) ) )
#define Instance()         ( ( PINSTANCE ) __LocalInstance )
#define STARDUST_INSTANCE  PINSTANCE __LocalInstance = InstancePtr();
```
