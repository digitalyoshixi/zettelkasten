---
tags:
  - virtualization
---
```
docker run -d -p 1024:1024 <tagname>
```
`-d` run in detached mode so it runs as a daemon process
`-p` signifies what host and what port it is running on
running `docker ps` will show that the image is running
![[Docker-20240702022105020.webp]]
`nc 127.0.0.1 1024` will connect to the container
```
docker run -d -p 1024:1024 -t <tagID>
```
![[Docker-20240910011418210.webp]]
```
docker run -it --privileged <tagname>
```
![[Docker-20240915002345746.webp]]