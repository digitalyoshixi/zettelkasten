---
tags:
  - virtualization
---
![[Docker-20240910012146560.webp]]
1. `docker ps` and note down the container ID
2. `docker exec -it <containerid> <app>`
	1. useful to make `<app>` be `/bin/sh` or `python`
Alternatively:
3. `docker images` and note down the container name
4. `docker run -it <containername> /bin/sh`. Note if you want programs like [[Vim]], you must install it in your docker-file