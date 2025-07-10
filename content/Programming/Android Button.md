---
tags:
  - android
---
A [[Android View|View]].
# Boilerplate
```xml
<Button  
    android:id="@+id/button"  
    android:layout_width="wrap_content"  
    android:layout_height="wrap_content"  
    android:onClick="onclickfunction"  
</Button>
```

```java
public void onclickfunction(View V){
	Log.d("my tag", "my log");
}
// ----- ALTERNATIVELY: -----
//create a variable that contain your button
Button button = (Button) findViewById(R.id.button);

    button.setOnClickListener(new OnClickListener(){
        @Override
        //On click function
        public void onClick(View view) {
            //Create the intent to start another activity
            Intent intent = new Intent(view.getContext(), AnotherActivity.class);
            startActivity(intent);
        }
    });
```