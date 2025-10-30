---
tags:
  - devops
---
![[Grafana-20251029013421837.webp|120]]
A dashboard to visualize data.
![[Grafana-20251029000614858.webp|526]]
# Installation
```
sudo apt-get install -y apt-transport-https software-properties-common wget

sudo mkdir -p /etc/apt/keyrings/

wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | sudo tee /etc/apt/keyrings/grafana.gpg > /dev/null

echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list

sudo apt-get update

sudo apt-get install grafana
```
# Configuration
Config file locate at `/etc/grafana/grafana.ini`
Ensure you edit such that:
```ini
[server]
domain = your-domain.com
# domain = 123.45.67.89
root_url = http://your-domain.com:3000
http_addr = 0.0.0.0
http_port = 3000
```
The initial username and password is `admin : admin`