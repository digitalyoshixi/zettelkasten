---
tags:
  - git
  - devops
---
# Setup
1. Create a new [[Linux Users]] called `webrunner`
2. ![[Github Runner-20250502215245781.webp]]
3. Click New self-hosted Runner and then copy the tutorial
# Service
```
[Unit]
Description=Run run.sh as webrunner
After=network.target

[Service]
Type=simple
User=webrunner
WorkingDirectory=/home/webrunner/actions-runner
ExecStart=/home/webrunner/actions-runner/run.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target
```