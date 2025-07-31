---
tags:
  - programming
---
This is a testing framework for testing java applications.
Can:
- Create [[Mock Objects]]
- Setup stubbing
- Verify behavior
# Gradle Import
```java
testImplementation "org.mockito:mockito-core:5.+"
```
# Boilerplate
```java
package com.safetyapp.mainapp;
import static org.mockito.Mockito.verify;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mock;
import org.mockito.junit.MockitoJUnitRunner;

@RunWith(MockitoJUnitRunner.class)
public class LoginMockitoTest {
    @Mock
    LoginActivity loginActivity;

}
```
# Concepts
- [[Mockito Spy]]
- [[Mockito Mock]]
- [[Mockito When]]
- [[Mockito Verify]]
- [[Mockito ThenReturn]]