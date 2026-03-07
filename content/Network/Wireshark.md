---
tags:
  - networking
  - security
---
Tool to analyze packets. Pivotal in retaliation and forensics.
### Profiles
Profiles are configurations of wireshark
![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivax_tmp_ced68987477385c8.png)
Changes colors, filters and more. Shift+CTRL+A to enter the configuration panel. There you can edit the profiles
![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivax_tmp_7ff215475ed7d5c7.png)
### Columns
You are able to edit the columns shown in the packet list. This allows you to also add more column parameters to make analysis easier like a column for UTC time.

CTRL+SHIFT+P > Columns
### Coloring rules

View > Coloring Rules

Allows change in the packet list for log colors so its not an ocean of blue.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivax_tmp_ebbb31c96725cb15.png)

Also order matters. Bad TCP will take priority over TCP SYN color.

### Filters

1. click this button at the top
    

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivax_tmp_893902bd14b4a63c.png)

2. Give it a label and a filter
    
3. At the side, click the label name
    

  

### TCP Segment Length > Length

TCP segment length is just superior to length in 99% of situations.

  

### Dumpcap

It's a terminal tool. To packet capture from eth0, type: dumpcap -i 1

To save these captures to a file, add a -w flag with the directory

To change file size limit of captures or captures per X, use the -b flag. -b filesize:500000 to allow filesizes up to 500mb. -b files:10 to allow up to 10 captures per cycle

  

### Conversations

Our PCAP files capture a lot! To read how each packet interacts with each other, we can use conversations.

Statistics > Conversations