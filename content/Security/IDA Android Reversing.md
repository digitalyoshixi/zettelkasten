---
tags:
  - flutter
  - android
  - reverse_engineering
---
After analyzing the file in blutter, you have IDA scripts.
1. Use [[apktool]] to get `libapp.so`, open this in IDA (get the x86_64 version!)
2. Use [[Blutter]] to get ida scripts `addNames.py`, run this script in [[IDA]]
