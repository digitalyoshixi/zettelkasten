---
tags:
  - redteam
  - web
---
### RESTAPI/HTTP request reading with burpsuite

Kali linux comes preinstalled with burpsuite. Make a temporary project for temporary purposes. Then allow the defaults

1. Kali comes preinstalled with burpsuite.
    
2. Make a temporary project. Allow defaults
    
3. Proxy
    
4. Open browser
    
5. Burpsuite will open up a chromium browser that it can monitor.
    
    1. Intercept is on
        
    2. Any redirect by the browser will be sent to burp suite first. So you can analyze then allow the redirect
        
6. Http history
    
7. Click on any api request to view what it sent