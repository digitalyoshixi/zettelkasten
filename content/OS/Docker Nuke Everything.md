---
tags:
  - docker
  - virtualization
---
```
# Stop all containers
sudo docker stop $(sudo docker ps -q)

# Remove all containers
sudo docker rm $(sudo docker ps -aq)

# Remove all images (optional - this will free up more space)
sudo docker rmi $(sudo docker images -q)

# Remove all volumes (optional - be careful, this removes data)
sudo docker volume prune -f

# Remove all networks (optional)
sudo docker network prune -f
```