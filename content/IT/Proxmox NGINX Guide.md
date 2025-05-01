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
### HTTPS Config File
1. Ensure that we have each certificate file in `/etc/nginx/ssl/` (cert and private key)
We can write a config file like:
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
		server_name yoshixi.net www.yoshixi.net;
		return 301 https://$host$request_uri;
	}
	server {
		listen 443 ssl;
		server_name yoshixi.net www.yoshixi.net;
		ssl_certificate /etc/nginx/ssl/pve-root-ca.pem;
		ssl_certificate_key /etc/nginx/ssl/pve-root-ca.key;

		ssl_protocols TLSv1.2 TLSv1.3;
		ssl_prefer_server_ciphers on;
		ssl_ciphers EECDH+AESGCM:EDH+AESGCM;
		ssl_session_cache shared:SSL:10m;
		ssl_session_timeout 180m;
		location / {
			proxy_pass http://192.168.2.66:3000;
		}
	}
}
```
7. `systemctl restart nginx`