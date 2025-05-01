---
tags:
  - IT
  - web
---
# Guide
### Installing Excalidraw
1. Create a [[LXC]] container
2. `apt-get install git curl nodejs npm`
3. `npm i -g yarn`
4. `git clone https://github.com/excalidraw/excalidraw.git`
5. `cd excalidraw`
6. `yarn`
7. `yarn start --host`
### Creating Autostart service
With [[systemD]]
### Creating CI/CD Pipeline