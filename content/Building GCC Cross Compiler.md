---
tags:
  - programming
  - os
---
# Process
### Get Source
```bash
git clone git://sourceware.org/git/binutils-gdb.git
```

```bash
git clone https://gcc.gnu.org/git/gcc.git
```
### Environment Variables
```bash
export PREFIX="$HOME/opt/cross"
export TARGET=i686-elf
export PATH="$PREFIX/bin:$PATH"
```
### Make Directories
```
mkdir -p ~/src/build-binutils
```
### Make Binutils
```bashpath/to/binutils-gdb/configure --target=$TARGET --prefix="$PREFIX" --with-sysroot --disable-nls --disable-werror --enable-default-execstack=no CXXFLAGS="-std=gnu++17" CFLAGS="-std=gnu17"
```