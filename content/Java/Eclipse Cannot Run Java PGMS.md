---
tags:
  - java
  - eclipse
---
I dont use eclipse, but this solves one of the most common problems.
You make a project, You make a class, and then you try running it, and it says something like:
`Unbound classpath container: 'JRE System Library [JavaSE-20]' in project Build path Build Path Problem`

This is how its fixed:
https://stackoverflow.com/questions/22921800/unbound-classpath-container-jre-system-library-java-se-6-1-6-0-65-b14-462
Project > Properties > Java Path Build
![[Eclipse Cannot Run Java PGMS-20231008010337423.webp]]
Java Build Path > Libraries > JavaSE-? > Edit...
![[Eclipse Cannot Run Java PGMS-20231008010431670.webp]]
Select Alternate JRE
![[Eclipse Cannot Run Java PGMS-20231008010522028.webp]]


Now you can run your programs
![[Eclipse Cannot Run Java PGMS-20231008010549553.webp]]