---
tags:
  - virtualization
---
# Installation
`sudo pacman -S docker-compose`
# Boilerplate
```
version: "5"
services:
    wsgi_server:
      build:
        context: ./wsgi-server/
        dockerfile: ./wsgi-server/Dockerfile
      image: wsgi-server:latest
      ports:
          - "3000:3000"
    blog:
      build:
        context: ./blog
        dockerfile: ./blog/Dockerfile
      image: blog:latest
      ports:
          - "8080:8080"
```
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