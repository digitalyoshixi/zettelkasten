---
tags:
  - networking
---
A method to simulate a network. Its recommended to use the virtual machine variant but, the setup for that is egregious


### Topology

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivb2_tmp_9328eed828adf707.png)

From top to bottom:

1. Routers
    
2. Switches
    
3. Devices
    
4. Security devices
    
5. All items
    
6. Link
    

You are going to be using most all of these. Switches for LAN, routers for WLAN security devices are optional

The most basic topology is a LAN. We use a switch to connect two PCs to each other.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivb2_tmp_7f0a9dbafb19ad18.png)

Do note that sometimes these green and red objects don't appear. If this happens, then resize the screen.

Additionally, you can go to View and check the boxes: “Snap to grid” and “Show grid” to make lining up devices much easier

  

### Running the topology

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivb2_tmp_dbee08cbc1e409f3.png)

Press the green arrow. Then, the red boxes in the topology display will turn to green circles.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivb2_tmp_4c3f10523d8189e7.png)

Click on a device(in this case I am on PC1 since that device is greyed out), Then press the command line button beside the green arrow. This will open up solar putty.

You can configure the fonts in solar putty by pressing the 3 dots at the side > settings > general > change font(launch putty) > windows > appearance > Font settings > change > OK > session > Default Settings > Save > Cancel

Anyways there are 2 devices that solar putty edits. PC1 and PC2. type the command: ip 10.1.1.1 255.255.255.0 on device PC1. type the command: 10.1.1.2 255.255.255.0 on device PC2. This sets up the ip addresses of these devices. Now you can ping to the other device. Lastly, type: save on each device to save the configurations to resume next time.

  

### GNS3 VM

To download the vm: [https://gns3.com/software/download-vm](https://gns3.com/software/download-vm)

Make sure the VM and your UI GNS3 have the same version, else they will not work together

To set up, follow these steps

1. In the UI, Edit > Preferences > GNS3 VM > Enable the GNS3 VM = True > Virtualization engine = VirtualBox