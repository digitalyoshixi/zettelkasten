---
tags:
  - automation
---
This is a tool for automation in DevOps. Compared to other automation tools like Ansible or SaltStack. Stackstorm automates via triggers/actions. An action is any task you give it, eg. hello word, snapshotting vm, sending notifications.

An action requires a rule. These are often yaml files. These files must contain a name and an action.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iv84_tmp_d934ae77829d44e4.png)

Now in order to fire these actions, you must login to stackstorm2. Run these commands:

1. st2 login st2admin --password idunno
    
2. st2 action list -p core
    

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iv84_tmp_56776031b1650fc5.png)

3. We can pick a package api to run. For example:

st2 run core.http url="[http://httpbin.org/get](http://httpbin.org/get)"

It will return what it finds on the webpage