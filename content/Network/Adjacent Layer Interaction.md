---
tags:
  - networking
  - networking_model
---
So say, a higher level protocol, HTTP wants the error recovery that TCP has. This lower level protocol TCP will have to provide the service for the higher level HTTP. The higher level protocol actually depends on the lower level one to do the work for it. It will give the task over to TCP, TCP will do what they do best and perform the function.