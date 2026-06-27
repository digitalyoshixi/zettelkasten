---
tags:
  - networking
  - linux
  - debian
---
A [[Jarkata Servlet|Java Servlet]] container to power web applications
![[Apache Tomcat-20260627155329056.webp]]
# Installation
https://www.digitalocean.com/community/tutorials/how-to-install-apache-tomcat-9-on-debian-10
### Get Java
1. `sudo apt update`
2. `sudo apt install default-jdk`
### Make User
`sudo groupadd tomcat`
`sudo useradd -s /bin/false -g tomcat -d /opt/tomcat tomcat`
### Fetch Tomcat
Version will depend. Go check what the most recent one is here:
https://downloads.apache.org/tomcat
1. `wget https://downloads.apache.org/tomcat/tomcat-9/v9.0.85/bin/apache-tomcat-9.0.85.tar.gz -P ~`
2. `sudo mkdir -p /opt/tomcat`
3. `sudo tar -xzf apache-tomcat-9.0.85.tar.gz  -C /opt/tomcat/`

### Change Perms
1. `sudo chown -R tomcat: /opt/tomcat`
2. `sudo chgrp -R tomcat /opt/tomcat`
3. `sudo find /opt/tomcat/tomcatapp/bin/ -type f -iname "*.sh" -exec chmod +x {} \;`
4. Find the java home **path**. `sudo update-java-alternatives -l`
5. `sudo nvim /etc/systemd/system/tomcat.service`
	write the following: 
```
[Unit]
Description=Apache Tomcat Web Application Container
After=network.target

[Service]
Type=forking

Environment=JAVA_HOME=/usr/lib/jvm/java-1.17.0-openjdk-amd64
Environment=CATALINA_PID=/opt/tomcat/temp/tomcat.pid
Environment=CATALINA_HOME=/opt/tomcat
Environment=CATALINA_BASE=/opt/tomcat
Environment='CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC'
Environment='JAVA_OPTS=-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom'

ExecStart=/opt/tomcat/bin/startup.sh
ExecStop=/opt/tomcat/bin/shutdown.sh

User=tomcat
Group=tomcat
UMask=0007
RestartSec=10
Restart=always

[Install]
WantedBy=multi-user.target
```
### Run Tomcat
1. `sudo systemctl daemon-reload`
2. `sudo systemctl enable --now tomcat`
### Firewall Policy
if you have [[Uncomplicated Firewall|ufw]]
`sudo ufw allow 8080/tcp`
# Open Tomcat
You can open tomcat with `http://the_server_ip:8080`