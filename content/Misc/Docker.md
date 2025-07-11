---
tags:
  - virtualization
---
Tool that creates lightweight environments called containers for app deployment. Docker is great at creating isolated spaces for your applications to run on while also providing them with OS level dependencies.
Great for:
- [[Microservices]]
# Concepts
- [[Containers]]
- [[Kubernetes Pod]]
- [[Dockerfile]]
- [[Docker Node]]
- [[Docker Compose]]
# Installation
### [[Arch Linux]]
1. `sudo pacman -S docker`
2. `sudo systemctl enable docker.service & sudo systemctl start docker.service` 
3. `sudo systemctl start docker.socket`
### Debian
1. `apt update`
2. `apt install ca-certificates curl`
3. `sudo install -m 0755 -d /etc/apt/keyrings`
4. `sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc`
5. `sudo chmod a+r /etc/apt/keyrings/docker.asc`
6. 
```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
7. `sudo apt-get update`
8. `sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`
# Using Docker
### Build Container
```
docker build -t <tagname> .
```
`-t` signifies the tag name. you can name this whatever you want
`.` indicates that the `Dockerfile` is within this directory. you can change this to be the directory name that has `Dockerfile` if its not in cwd
Use `docker images` to view all created images.
![[Pasted image 20240701222113.png]]
### Buildx Container
`sudo pacman -S docker-buildx`
```
docker build -t <tagname> .
```
### Run Container
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
### Stop Container
`docker container stop <id>`
![[Docker-20240702022538807.webp]]
### Delete Image
Use `docker images` to list all images then,
`docker rmi -f <id>`
![[Docker-20240720180345801.webp]]
### Open Container In App
![[Docker-20240910012146560.webp]]
1. `docker ps` and note down the container ID
2. `docker exec -it <containerid> <app>`
	1. useful to make `<app>` be `/bin/sh` or `python`
Alternatively:
3. `docker images` and note down the container name
4. `docker run -it <containername> /bin/sh`. Note if you want programs like [[Vim]], you must install it in your docker-file
### Copy Files to Host Machine
![[Docker-20250711220025059.webp]]
```
sudo docker cp id:/filepath /hostfilepath
```
# Practical Use Cases
- Make a [[Docker Compose]] file which automates the process of creating gitlab servers
- You can use docker like a linux server where you SSH into