---
tags:
  - linux
  - forensics
aliases:
  - ewf
---
A collection of tools to work with [[Expert Witness Compression Format|EWF]].
# Installation
```
sudo pacman -S libewf
```
# Usage
You get a bunch of commands:
- `ewfacquire`
- `ewfdebug`
- `ewfinfo`
- `ewfrecover`
- `ewfacquirestream`
- `ewfexport`
- `ewfmount`
- `ewfverify`
### Verify Image Hash
```
ewfverify -d sha1 ./myimage.E01
```
### Mount Image into Folder
```
mkdir phy1
mkdir log1
sudo ewfmount ./myimage.E01 ./phy1
```