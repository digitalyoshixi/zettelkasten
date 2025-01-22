---
tags:
  - networking
  - linux
---
A client less remote access gateway to access your remote desktop through a web browser.
It is client less and does not require you to download any software other than your built in web browser to use. 
# Install Dependencies
https://guacamole.apache.org/doc/gug/installing-guacamole.html
`sudo apt install libcairo2-dev libjpeg62-turbo-dev libpng-dev libtool-bin uuid-dev libavcodec-dev libavformat-dev libavutil-dev libswscale-dev freerdp2-dev libpangol1.0-dev libvncserver-dev libpulse-dev libvorbis-dev libwebp-dev libssl-dev build-essential`
### Install Tomcat
[[Apache Tomcat]]
# Install Guacamole
https://guacamole.apache.org/doc/gug/installing-guacamole.html
### Build Server
Version depends. check https://downloads.apache.org/guacamole/ for the most recent version. It should be in the [/source] section
1. `wget https://downloads.apache.org/guacamole/1.5.4/source/guacamole-server-1.5.4.tar.gz -P ~`
2. `tar xzf ~/guacamole-server-1.5.4.tar.gz`
3. `cd guacamole-server-1.5.3`
4. `./configure --disable-guacenc --with-init-dir=/etc/init.d`
5. `make`
6. `sudo make install`
7. `sudo ldconfig`
8. `sudo systemctl daemon-reload`
9. `sudo systemctl start guacd`
10. `sudo systemctl enable guacd`
### Get Client/Webapp
1. `sudo mkdir /etc/guacamole`
2. `wget https://downloads.apache.org/guacamole/1.5.4/binary/guacamole-1.5.4.war -P ~`
3. `sudo mv ~/guacamole-1.5.4.war /etc/guacamole/guacamole.war`
**BE SURE TO NAME IT guacamole.war**. If you dont, then when you get on the website, it will show up as a different name.
5. `sudo ln -s /etc/guacamole/guacamole.war /opt/tomcat/tomcatapp/webapps/`
### Configure Guacamole Server
1. `echo "GUACAMOLE_HOME=/etc/guacamole" | sudo tee -a /etc/default/tomcat`
2. `echo "export GUACAMOLE_HOME=/etc/guacamole" | sudo tee -a /etc/profile`
3. `sudo nvim /etc/guacamole/guacamole.properties`
4. Write the following: 
```
guacd-hostname: localhost guacd-port: 4822 user-mapping: /etc/guacamole/user-mapping.xml auth-provider: net.sourceforge.guacamole.net.basic.BasicFileAuthenticationProvider
```
4. `sudo ln -s /etc/guacamole /opt/tomcat/tomcatapp/.guacamole`
5. `sudo chown -R tomcat: /opt/tomcat/`
### Guacamole Authentication
##### Make a password 
`echo -n cheeseburglar201@$ | openssl md5`
##### Write User Auth
`sudo nvim /etc/guacamole/user-mapping.xml`
keep this encrypted password, it will be used below.

write the following:
```
<user-mapping>

    <!-- Another user, but using md5 to hash the password
         (example below uses the md5 hash of "PASSWORD") -->
    <authorize
            username="someguacuser"
            password="THEENCRYPTEDPASSWORDFROMABOVE"
            encoding="md5">

        <!-- First authorized connection -->
        <connection name="Debian RDP Friend Server">
            <protocol>rdp</protocol>
            <param name="hostname">66.212.170.222</param>
            <param name="port">3389</param>
            
        </connection>

        <!-- Second authorized connection -->
		<connection name="localhost">
            <protocol>vnc</protocol>
            <param name="hostname">localhost</param>
            <param name="port">5901</param>
            <param name="password">VNCPASS</param>
        </connection>

    </authorize>

</user-mapping>
```
### Restart Tomcat
1. `sudo systemctl restart tomcat guacd`
# Open Guacamole
`http://the_server_url:8080/guacamole`

# Guacamole logs
To diagnose issues involving guacamole:
`sudo cat /var/log/daemon.log | less`
configure your `/etc/guacamole/user-mapping.xml` or `/etc/guacamole/guacd.conf` or `/etc/guacamole/guacamole.properties` accordingly
Then `sudo systemctl daemon-reload` , `sudo systemctl restart tomcat guacd`