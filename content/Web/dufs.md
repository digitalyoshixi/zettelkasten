---
tags:
  - IT
  - web
---
This is a file server capable of service static files.
# Installation
1. 
```
git clone https://github.com/sigoden/dufs.git
```
2. 
```
docker run -v `pwd`:/data -p 5000:5000 --rm sigoden/dufs /data -A
```
# Running a both a read and write server
```
docker run -d -v --restart unless-stopped `pwd`:/data -p 5000:5000 sigoden/dufs /data -A -p 5000
docker run -d -v --restart unless-stopped `pwd`:/data -p 4000:4000 sigoden/dufs /data -p 4000
```
