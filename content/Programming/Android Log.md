---
tags:
  - android
---
The logging library that works with [[Android SDK|Android Studio]].

```java
import android.util.Log;

public class MainActivity extends AppCompatActivity{
	public void myfunc(){
		Log.d("my tag","my logging message");
	}
}
```
The information will be shown in the [[Logcat]] menu