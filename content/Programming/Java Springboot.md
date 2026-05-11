---
tags:
  - java
  - programming
  - web
aliases:
  - Springboot
---
This is a web framework to develop application backends in [[Java]].
A easier version of creating [[Java Spring]] [[eXtensive Markup Language|XML]].
Uses [[Apache Tomcat]] under the hood.
Better for [[Microservices]].
![[Java Springboot-20251003140809092.webp]]
# Initialization
https://start.spring.io/
Add the dependency:
- Spring Web
# Boilerplate
```java
@RestController
@RequestMapping("/api")
public class MyController {
    @GetMapping("/hello")
    public String sayHello() {
        return "Hello, World!";
    }
}
```
# Concepts
- [[Dependency Injection]]
- [[Aspect Oriented Programming]]
- [[Spring Data]]
- [[Spring Data Java Persistence API|JPA]]
- [[Controller Layer|Presentation Layer]]
- [[Service Layer|Business Logic Layer]]
- [[Repository Layer]]
- [[Model Layer]]
- [[Database Layer]]
- [[Model-View-Presenter]]
- [[Inversion of Control]]
# Common Endpoints
- `/env`
- `/info`
- `/mappings`
- `/httptrace`
- `/logfile`
- `/heapdump`