---
tags:
  - networking
---
Curl is the swiss army knife of web requests.
`curl "http://some.ip.you.have:theport"`
### Sending a http request 
`curl "http://127.0.0.1:80"`
sends http req on port 80
If you have a web application with [[Application Endpoints]] then it can get responses
![[Curl-20241004032152668.webp]]
### POST Requests
```
curl -X POST http://127.0.0.1:5000/greet/david
```
##### JSON
```
curl -X POST -H "Content-Type: application/json" -d '{"name" : "david"}' http://127.0.0.1:3000/api/products
```
##### Form
```
curl -X POST https://reqbin.com/echo/post/form
   -H "Content-Type: application/x-www-form-urlencoded" 
   -d "param1=value1&param2=value2" 
```
##### File
```
curl -F 'image=@./perplexed' http://127.0.0.1:5000/genai/image
```
### Get Headers Only
```
curl -I http://127.0.0.1:5000/hello
```
![[Curl-20241004034547712.webp]]
### Allow Insecure
```
curl -k http://site.com
```
Does not care about [[Hyper Text Transfer Protocol Secure|HTTPS]], [[Secure File Transfer Protocol|SFTP]], [[Secure Copy|SCP]]
### Websocket Sending
```
curl --no-buffer \ --include \ --websocket \ -d '{"action": "subscribe", "topic": "updates"}' \ ws://localhost:8080/ws
```
Alternatively use [[websocat]]