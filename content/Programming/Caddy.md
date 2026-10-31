---
tags:
  - programming
  - web
---
A simple open source web server and load balancer.
Uses [[Declarative Programming]] with `Caddyfile`.
# Enabling Caddy File
```
cd /path/to/caddyfile_directory
caddy run 
```
# Caddyfile Template
```
:80 {
	root * /var/www/mysitedirectory
	# enable file server
	file_server
}
```