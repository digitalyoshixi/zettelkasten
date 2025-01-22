---
tags:
  - java
---
# Installation(Windows)
https://phoenixnap.com/kb/install-maven-windows 
1. Download the latest binary zip files
2. Move that folder to Program Files
3. Set [[Windows Environment Variables]] to include the maven folder
4. type `mvn --version` in command line
5. make sure [[JAVA_HOME]] is set up
# VSCode with Maven
https://www.youtube.com/watch?v=zlHXH6maOR0
1. Make a new maven project. defaults with maven quickstart, 1.4, give it a package name, give it a folder name, then pick its parent folder.
2. Just click enter here. and then type Y ![[Maven For Java-20240115034121675 1.webp]]
3. Put all your java shit in here ![[Maven For Java-20240115040239070 1.webp]]

# Adding new jar dependencies
1. use sonatype or mvnrepository
##### Sonatype
https://central.sonatype.com/ 
Just search for it, then copy this portion
![[Maven For Java-20240115034941513 1.webp|611]]
##### mvnrepository
![[Maven For Java-20240115035124699 1.webp|514]]
![[Maven For Java-20240115035138005 1.webp|510]]
2. paste this snippet in the pom.xml file of your maven project
![[Maven For Java-20240115035218099 1.webp]]

# Adding Repositories
Dont be shy, just put it in pom.xml
![[Maven For Java-20240115035702886 1.webp|504]]