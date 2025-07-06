---
tags:
  - android
---
# XML
```xml
<TextView  
    android:id="@+id/textView"  
    android:layout_width="wrap_content"  
    android:layout_height="wrap_content"  
    android:text="TextView"  
    />
```
# Activity
```java
import android.widget.TextView;
//...
(TextView) myText = findViewById(R.id.textView);
myText.setText("my message");
```