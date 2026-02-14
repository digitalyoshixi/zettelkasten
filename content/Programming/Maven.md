---
tags:
  - java
---
A package managing system for [[Java]] projects.
# Installation
### Windows
https://phoenixnap.com/kb/install-maven-windows 
1. Download the latest binary zip files
2. Move that folder to Program Files
3. Set [[Windows Environment Variables]] to include the maven folder
4. type `mvn --version` in command line
5. make sure [[JAVA_HOME]] is set up
### [[Arch Linux]]
1. `sudo pacman -S maven`
# Setup Maven Project
1. 
```
mvn archetype:generate -DgroupId=cscb07 -DartifactId=lab4 -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.5 -DinteractiveMode=false
```
1. You should have the following folders in `/src`:
   ![[Maven-20250609135552088.webp]]
2. Run `mvn compile`
3. You can run `cd /target/classes` and then run the compiled classes
   ![[Maven-20250609135944522.webp]]
4. Run `mvn test` to run each test file within the test folder, and get a test results output
# Guides
- [[VSCode Maven]]
