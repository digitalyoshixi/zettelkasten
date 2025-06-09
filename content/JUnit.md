---
tags:
  - java
---
This is a testing library for [[Java]].
You can run tests with [[Maven]], by using `mvn test`
# Dependency with [[Maven]]
```xml
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.13.2</version>
    <scope>test</scope>
</dependency>
```
# Example
```java
import static org.junit.jupiter.api.Assertions.*;
public class Tester(){
	@Test
	public void testEquals(){
		assertEquals(2,2); // ok!
	}
	@Test
	public void testTrue(){
		assertTrue(True); // ok!
	}
	@Test
	public void testFalse(){
		assertFalse(False); // ok!
	}
}
```
