---
tags:
  - IT
---
A cloud storage drop-box like tool.
# Installation
https://nextcloud.com/blog/how-to-install-the-nextcloud-all-in-one-on-linux/
1. Install [[Docker]] (`curl -fsSL https://get.docker.com | sudo sh`)
2. 
```
sudo docker run \
--sig-proxy=false \
--name nextcloud-aio-mastercontainer \
--restart always \
--publish 80:80 \
--publish 8080:8080 \
--publish 8443:8443 \
--volume nextcloud_aio_mastercontainer:/mnt/docker-aio-config \
--volume /var/run/docker.sock:/var/run/docker.sock:ro \
ghcr.io/nextcloud-releases/all-in-one:latest
```
3. Site should be up on `https://localhost:8080`