---
tags:
  - programming
  - web
---
1. 
```
sudo nvim /etc/nginx/sites-available/mywebsite
```
2. 
```
server {
    listen 80;
    server_name mywebsite.com www.mywebsite.com;

    root /var/www/mywebsite;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```
3. 
```
sudo ln -s /etc/nginx/sites-available/mywebsite /etc/nginx/sites-enabled
```
4. Move your site directory to be `/var/www/mywebsite`
5. Test with
```
sudo nginx -t
```
6. 
```
sudo systemctl reload nginx
```
