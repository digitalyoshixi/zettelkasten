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
@ExtendWIth(MockitoExtension.class)
public class MockitoTest{
	@Mock
	List<String> mockList;

	@Test
	void mock_list_returns_correct_element(){
		when(mockList.get(0)).thenReturn("Like");
		assertEquals("Like", mockList.get(0));
	}
}
```