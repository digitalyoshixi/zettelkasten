---
tags:
  - security
---
A frida module that provides functionality to intercept function calls and write hooks.
# Callbacks
- `onEnter`: allows us to see/modify input values
- `onLeave`: allows us to see/modify return values
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