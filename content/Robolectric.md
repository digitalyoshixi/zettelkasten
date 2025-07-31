---
tags:
  - android
  - programming
---
A testing framework that has access to android runtime environment.
# Gradle
```
android {
  testOptions {
    unitTests {
      includeAndroidResources = true
    }
  }
}

dependencies {
  testImplementation 'junit:junit:4.13.2'
  testImplementation 'org.robolectric:robolectric:4.15'
}
```
# Boilerplate
```java
@RunWith(RobolectricTestRunner.class)
public class WelcomeActivityTest {
    @Test
    public void clickingLogin_shouldStartLoginActivity() {
        try (ActivityController<WelcomeActivity> controller = Robolectric.buildActivity(WelcomeActivity.class)) {
            controller.setup(); // Moves the Activity to the RESUMED state

            WelcomeActivity activity = controller.get();
            activity.findViewById<Button>(R.id.login).performClick();

            Intent expectedIntent = new Intent(activity, LoginActivity.class);
            Intent actual = shadowOf(RuntimeEnvironment.application).getNextStartedActivity();
            assertEquals(expectedIntent.getComponent(), actual.getComponent());
        }
    }
}
```