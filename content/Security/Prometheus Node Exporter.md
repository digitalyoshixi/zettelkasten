---
tags:
  - devops
---
A [[systemD|Linux Service]] that exports hardware and kernel-related metrics.
# Setup User
```
sudo adduser prometheus
sudo usermod -aG sudo prometheus
```
# Setup on Container
1. 
```
wget https://github.com/prometheus/node_exporter/releases/download/v1.10.2/node_exporter-1.10.2.linux-amd64.tar.gz
```
2. 
```
tar xvfz node_exporter-*.*-amd64.tar.gz
```
3. 
```
cd node_exporter-1.10.2.linux-amd64/
```
3. 
```
mv node_exporter /opt/node_exporter
```
4. 
```
sudo ln -s /opt/node_exporter /usr/local/bin/node_exporter
```
5. 
```
sudo vim /etc/systemd/system/node-exporter.service
```
With:
```
[Unit]
Description=Prometheus Node Exporter
After=network-online.target

[Service]
User=prometheus
Restart=on-failure
ExecStart=/usr/local/bin/node_exporter

[Install]  
WantedBy=multi-user.target
```
6. 
```
sudo systemctl daemon-reload
sudo systemctl enable node-exporter
sudo systemctl start node-exporter
```
6. 
You can access it from:
```
curl http://localhost:9100/metrics | grep "node_"
```
### Setup Prometheus
```
global:
  scrape_interval:     15s
  external_labels:
    monitor: 'codelab-monitor'
scrape_configs:
  - job_name: 'prometheus'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:9090']
  - job_name: 'lxc-containers'
    static_configs:
      - targets: 
          - '192.168.2.69:9100'
```