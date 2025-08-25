---
tags:
  - virtualization
---
```
docker build -t <tagname> .
```
`-t` signifies the tag name. you can name this whatever you want
`.` indicates that the `Dockerfile` is within this directory. you can change this to be the directory name that has `Dockerfile` if its not in cwd
Use `docker images` to view all created images.
![[Pasted image 20240701222113.png]]