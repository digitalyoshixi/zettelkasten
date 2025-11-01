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

### Setting up Prometheus
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
  - job_name: 'snmp_exporter'
    metrics_path: /snmp
    params:
      module: [if_mib]
    static_configs:
      - targets:
          - 192.168.2.69 # target IP
    relabel_configs:   
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: 127.0.0.1:9116 # SNMP Exporter
```