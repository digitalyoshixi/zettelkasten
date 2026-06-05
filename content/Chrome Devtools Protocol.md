---
tags:
  - web
  - programming
aliases:
  - CDP
---
Running the chrome browser in devmode to expose APIs.
# Running
```
chrome --remote-debugging-port=9222 \
--user-data-dir=/tmp/chrome-debug-$$ \
--no-first-run \
--no-default-browser-check \
--remote-allow-origins='*'
```
# Getting Websocket URL
```
curl -s http://127.0.0.1:9222/json | grep -i "webSocketDebuggerUrl"
```