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
### Simple Config File
```
worker_processes auto;
pid /run/nginx.pid;
error_log /var/log/nginx/error.log

events {
	worker_connections 768;
	# multi_accept on;
}
http {
	server{
		listen 80;
		location / {
			proxy_pass http://192.158.2.66:3000;	
		}	
	}

}
```
Note that right now, it points to my webserver running excalidraw on my local device.
### Better SSL Config File
1. Ensure that we have each certificate file in `/etc/nginx/ssl/`
```
# From Proxmox host
pct push <YOUR-LXC-ID> /etc/pve/pve-root-ca.pem /etc/nginx/ssl/<certname>.pem
pct push [YOUR-LXC-ID] /etc/pve/priv/pve-root-ca.key /etc/nginx/ssl/<cername>.key
```
We can write a config file like:
```

```
7. `systemctl restart nginx`