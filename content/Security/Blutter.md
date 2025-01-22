---
tags:
  - flutter
  - reverse_engineering
---
A reverse engineering tool to decompile and return the sources files for a given flutter .apk file.
# Installation
1. https://github.com/worawit/blutter
2. Download source code
# Utilization
run `python blutter.py <app>.apk <outdir> --rebuild`
This will return the:
- disassembly located in `asm/`
- [[Frida]] script named `blutter_frida.js`
- [[IDA]] scripts.
- `objs.txt` for rough information about objects
- `pp.txt` for object pool information
### Tips
- [[Blutter Finding Function Definitions]]
- [[IDA Android Reversing]]