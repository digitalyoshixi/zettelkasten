---
tags:
  - web
---
1. Create a [[LXC]] container with [[Debian]]
2. `apt-get install nginx vim`
3. `systemctl enable nginx`
4. `systemctl start nginx`
5. The nginx website should be visible
   ![[Proxmox NGINX Guide-20250501014947036.webp]]
6. Lets create a reverse proxy now. `vim /etc/nginx/nginx.conf`