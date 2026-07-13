---
tags:
  - virtualization
---
# Installation
`sudo pacman -S docker-compose`
# Building Compose
```
docker compose build
```
# Setup Docker Instance
```
docker compose up -d
```
- This will take down the service to rebuild first, so you should `docker compose build` first!
# Take Down
```
docker compose down
```