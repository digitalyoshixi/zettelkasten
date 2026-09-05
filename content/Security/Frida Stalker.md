---
tags:
  - security
---
A code tracing engine using [[Frida]].
Uses [[Dynamic Recompilation]] 
# Script
```js
Process.enumerateThreads().forEach(function (thread) {
    Stalker.follow(thread.id, {
        events: {
            call: false,    // set to true to trace function calls
            ret: false,
            exec: false     // set to true to trace every executed instruction
        },
        onReceive: function (events) {
            // Parse and parse the events or dump to disk
            console.log("Stalker event received.");
        }
    });
});
```