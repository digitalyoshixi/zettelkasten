---
tags:
  - android
---
A catch-all term that involves the intention of this data being used.
Can allow:
- Data transfer between [[Android Screen]]
# Intents to Change Screen
### Routing File
```java
public void navigateIntent(View v){  
    Intent i = new Intent(this, SettingsActivity.class);  
    // send data to next activity
	i.putExtra("mykey", "myvalue");
	// route to next activity
    startActivity(i);  
}
```
### Destination File
```java
public class SettingsActivity extends AppCompatActivity{  
    @Override  
    protected void onCreate(Bundle savedInstanceState){  
	    // ... boilerplate
        Intent i = getIntent();
        String message = i.getStringExtra("mykey");
    }  
}
```
