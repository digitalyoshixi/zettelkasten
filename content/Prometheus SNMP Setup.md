---
tags:
  - devops
---
# Procedure
### Setting up User
```
sudo adduser prometheus
sudo usermod -aG sudo prometheus
```
### Getting Binary Setup
1. 
```
wget https://github.com/prometheus/snmp_exporter/releases/download/v0.29.0/snmp_exporter-0.29.0.linux-amd64.tar.gz
```
2. 
```
tar xzf snmp_exporter-0.29.0.linux-amd64.tar.gz 
```
3. 
```
sudo mv snmp_exporter-0.29.0.linux-amd64 /opt/snmp_exporter
```
4. 
```
sudo ln -s /opt/snmp_exporter/snmp_exporter /usr/local/bin/snmp_exporter
```
### Creating Service
1. 
```
sudo vim /etc/systemd/system/snmp-exporter.service
```
2. 
```
[Unit]
Description=Prometheus SNMP Exporter
After=network-online.target

[Service]
User=prometheus
Restart=on-failure
ExecStart=/usr/local/bin/snmp_exporter --config.file /opt/snmp_exporter/snmp.yml

[Install]  
WantedBy=multi-user.target
```
3. 
```
sudo systemctl daemon-reload
sudo systemctl enable snmp-exporter
sudo systemctl start snmp-exporter
```