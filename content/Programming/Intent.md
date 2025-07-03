---
tags:
  - android
---
A catch-all term that involves the intention of this data being used.
Can allow:
- Data transfer between [[Android Screen]]
# Intents to Change Screen
```java
public void navigateIntent(View v){  
    Intent i = new Intent(this, SettingsActivity.class);  
    // send data to next activity
	i.putExtra("mykey)
	// route to next activity
    startActivity(i);  
}
```
