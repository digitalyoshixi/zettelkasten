---
tags:
  - networking
  - IT
---
## VPN Protocol
We must choose the VPN protocol we want to use first and foremost.
https://www.ivpn.net/pptp-vs-ipsec-ikev2-vs-openvpn-vs-wireguard/
For us, we have 4 choices that have good support.
1. PPTP
2. IPSec IKEv2
3. OpenVPN
4. WireGuard

Wireguard is the most secure, but it is not runnable on linux unfortunately.
We will use OpenVPN.
# Setting up security on Debian
## VPN Account
Simply create an account on the OS.
### Make account
`su -`
`useradd -m [username]`
`passwd [username]`
### Wheel group
Then add them to the wheel group
To make the wheel group, first type: `groupadd wheel`
Then add them `usermod -G wheel [username]`
finally, go to edit /etc/sudoers file
`vim /etc/sudoers`
and add the following lines:
![[Pasted image 20230913193532.png]]
Ok save it with `w!` and then quit `q!`
### Enter the new account
to enter the new account, type `su [username]`
and then enter the home directory: `cd ~`
## SSH Keys
Enter you client machine. Linux machine, or use WSL.
### Making .ssh
https://stackoverflow.com/questions/15190391/ssh-directory-not-being-created
If you have not ssh into another computer on this computer before, then you will have to make your own .ssh folder. it is very simple. go to your home directory and make a .ssh folder
`mkdir ~/.ssh`
and also,
`chmod 700 ~/.ssh`
### Keygen
enter the .ssh directory
`cd .ssh`
we are making an rsa key with 4096 bits.
![[Pasted image 20230913200310.png]]
Recommended to give your vpn file a name. in my case it is DAVpn.
### \*.pub
`ls -a`
![[Pasted image 20230913200532.png]]
We need to copy this to our **Remote VPN** 
#### SSH test
to do this, we need to be able to ssh into it first. do a quick test of ssh into it

On your VPN machine, type: `ip a`
and then locate the text after 'inet'. that will be your IP.
![[word-image-146.webp]]

Back on your client machine, try and ssh into your VPN.
`ssh [username]@[ip]`
for me, i did:
![[Pasted image 20230913201237.png]]
If SSH test works, then you can securely copy a file to it.
#### Secure copy
![[Pasted image 20230913201719.png]]
`scp [pubfile] [username]@[ip]:`
make sure to have the colon at the end. 

Now, if I `ls` in the VPN machine, I can see the .pub file.
![[Pasted image 20230913202235.png]]
### VPN Machine SSH setup
Make sure you also make a .ssh folder on the VPN machine as well. with permissions 700.
And then, make a `authorized_keys` file in the .ssh directory.
![[Pasted image 20230913202905.png]]
`touch ~/.ssh/authorized keys`
and then pipe your .pub file into that new file you made.
![[Pasted image 20230913204341.png]]
`cat [.pubfile] >> ~/.ssh/authorized_keys`
And then, lets edit the configs of our sshdconfig.
![[Pasted image 20230913204512.png]]
With great power comes great responsibility
We are surgeons. This is the task:
![[Pasted image 20230913205017.png]]
![[Pasted image 20230913205147.png]]
![[Pasted image 20230913205431.png]]
```
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthenticaton no
AuthorizedKeysFile .ssh/authorized_keys .ssh/authorized_keys2
```
we disable password authentication as clear text passwords. we want maximum security.

You can also change the port. the default ssh port is 22. we like that, leave it as is.
now we restart the sshd
`sudo systemctl restart sshd`
`sudo reboot`

ssh into the vpn on the Client machine.
![[Pasted image 20230913214024.png]]
you will need the ssh file this time
# Making the VPN
we are using OpenVPN.
![[Pasted image 20230913214219.png]]
`sudo apt install openvpn`
We will use an install script for openvpn.
https://raw.githubusercontent.com/angristan/openvpn-install/master/openvpn-install.sh
in our ssh'ed session, or you could just do this on the VPN machine itself, you use curl commands to download.
`curl -LJO https://raw.githubusercontent.com/angristan/openvpn-install/master/openvpn-install.sh`
![[Pasted image 20230913214803.png]]
`chmod +x openvpn-install.sh`
and then run the script as root
`sudo ./openvpn-install.sh`
I used all the default settings.
my client name is desktop and its passwordless.
![[Pasted image 20230913215337.png]]
## No log VPN
We dont want to store logs.
![[Pasted image 20230913215845.png]]
`sudo vim /etc/openvpn/server.conf`
![[Pasted image 20230913215933.png]]
change verb 3 to verb 0

and finally restart the service 
`sudo systemctl restart openvpn`
## Download .ovpn file
![[Pasted image 20230913220244.png]]
so we are on the client machine. instead of ssh, we are sftp to connect into it.
same sort of deal, you dont need to colon to connect now tho.
To download this,
![[Pasted image 20230913220411.png]]
`get [clientname].ovpn`
ok, exit out of this session back into the client machine

install openvpn on the client machine too.
![[Pasted image 20230913220620.png]]

## Connection
![[Pasted image 20230913220716.png]]
`sudo openvpn --config desktop.ovpn`
Now, this is only for my WSL. I cant even change my ip on actual windows. the IP for the WSL and the actual windows machine is different.