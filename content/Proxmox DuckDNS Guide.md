---
tags:
  - web
  - IT
---
# Guide
1. Get a domain at www.duckdns.org
   ![[Proxmox DuckDNS Guide-20250501024408378.webp]]
2. Create a [[LXC]] for duckdns
3. We setup a [[Cron|Cronjob]] to automatically update your ip address
4. `apt-get install curl`
5. `mkdir duckdns`
6. `vim duckdns/duck.sh`
7. With contents:
```bash
#!/bin/bash
DOMAIN="EXAMPLE"
TOKEN="TOKEN"
echo url="https://www.duckdns.org/update?domains=$DOMAIN&token=$TOKEN&ip=" | curl -o ~/duckdns/duck.log -K -
```
8. `crontab -e` and add `**/5 * * * * ~/duckdns/duck.sh >/dev/null 2>&1*`
9. Now, to see if this works, I want to add port forwarding for my proxmox console to see if i can view it from outside.
   ![[Proxmox DuckDNS Guide-20250501030221712.webp]]
   
   ![[Proxmox DuckDNS Guide-20250501030315868.webp]]
# Sources
- https://gist.github.com/zidenis/e93532c0e6f91cb75d429f7ac7f66ba5
- https://gist.github.com/taichikuji/6f4183c0af1f4a29e345b60910666468