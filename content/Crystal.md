---
tags:
  - programming
---
A basic general purpose programming language.
- [[Ruby]]-like syntax
- Compiles to [[Low Level Virtual Machine|LLVM]]
# Installation

### Debian 12
1. `echo 'deb http://download.opensuse.org/repositories/devel:/languages:/crystal/Debian_12/ /' | sudo tee /etc/apt/sources.list.d/devel:languages:crystal.list`
2. `curl -fsSL https://download.opensuse.org/repositories/devel:languages:crystal/Debian_12/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/devel_languages_crystal.gpg > /dev/null`
3. `sudo apt update`
4. `sudo apt install crystal1.11`
