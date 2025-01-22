---
tags:
  - linux
  - debian
---
TAR
## Installing TGZ files (debian linux)

1. sudo apt update && sudo apt upgrade -y
    
2. sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
3. `tar -xf tgzfilename.tgz`
    
4. Run the configure script if there is one
    
5. sudo make Makefile
    
6. Sudo make install