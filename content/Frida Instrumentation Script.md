---
tags:
  - security
---
The script that takes care of interactions with the running process.
- Written in [[JavaScript]]
- Intercepts function calls
- Can be used to monitor instructions/functions
# Example
```js
const targetAddress = Process.getModuleByName('kernel32.dll').findExportByName('CreateFileW');

Interceptor.attach(targetAddress, {
    onEnter: function(args) {
        console.log('CreateFileW hit');
        console.log('  path:', args[0].readUtf16String());
    },
    onLeave: function(retval) {
        console.log('return:', retval.toInt32());
    }
});
```