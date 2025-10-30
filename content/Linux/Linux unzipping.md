---
tags:
  - file
  - compression
  - linux
---
### Zip files
`sudo pacman -S unzip`
- `unzip somearchive.zip`
- `unzip`
- `unzip -p mypassword file.zip`
##### Allow Zipbomb
`export UNZIP_DISABLE_ZIPBOMB_DETECTION=TRUE`
### Rar files
`sudo pacman -S unrar`
`unrar x somearchive.zip`
### Tarball (gz)
`tar -xf somearchive.tar.gz`
### Tarball (zst)
`tar --use-compress-program=unzstd -xvf somearchive.tar.zst`
