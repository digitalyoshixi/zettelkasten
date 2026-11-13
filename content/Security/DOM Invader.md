---
tags:
  - security
  - web
---
A tool to automatically find prototype pollution.
# Setup
1. Open burp browser
2. Extensions > Dom Invader > Toggle 'Dom invader is on'
3. Extensions > Dom invader > Attack Types > Prototype Pollution On
4. Open devtools > Dom Invader Tab > Reload page
![[DOM Invader-20261113022300499.webp]]
5. Scan for gadgets > Wait > Open Devtools in that tab
![[DOM Invader-20261113022353230.webp]]
6. Exploit, you should get an alert
![[DOM Invader-20261113022411024.webp]]