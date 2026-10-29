---
tags:
  - web
  - security
---
A [[Burp Suite]] extension to improve the speed of requests with [[Burp Suite Intruder]].
# Request Format
- `%s` to be a replacement 
# Sniper Attack
```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint)

    for word in open('/usr/share/dict/words'):
        engine.queue(target.req, word.rstrip())

def handleResponse(req, interesting):
    table.add(req)
```
# Single Packet Attack
```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                            concurrentConnections=1,
                            engine=Engine.BURP2
                            )
    
    # queue 20 requests in gate '1'
    for i in range(20):
        engine.queue(target.req, gate='1')
    
    # send all requests in gate '1' in parallel
    engine.openGate('1')
```