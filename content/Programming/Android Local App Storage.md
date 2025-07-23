---
tags:
  - android
aliases:
  - Android Context Files Directory
---
# Accessing Local Storage
```java
Context ctx = appcontext.getContext()
File myfile = new File(ctx.getFilesDir(), "questionresults.json");
```
# Location
1. Open Device Manager
2. Open in device explorer
   ![[Android Local App Storage-20250722203759657.webp]]
3. Open `/data/data/com.safetyapp.mainapp/files/questionresults.json`
   