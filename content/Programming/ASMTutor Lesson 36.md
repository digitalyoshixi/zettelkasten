---
tags:
  - web
  - ASMTutor
  - x86
  - networking
  - syscall
---
### Lesson 36 webpages

To connect to a remote webpage, we must do the following:

1. Create an active socket that we will use to send outbound requests
    
2. Connect our socket with a socket on the remote webpage
    
3. Send a http formatted request from our socket to their webserver
    
4. Recieve the http formatted response from webserver
    

  

An http formatted request is split into 3 sections:

1. Line containing requrest method, request url and http version
    
2. Optional section of request headers
    
3. Empty line. Tells remote server you have finished sending request
    

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivcx_tmp_ca07b51da48a3826.png)