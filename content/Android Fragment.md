---
tags:
  - android
aliases:
  - Fragment
---
These are small [[Android Screen Activity|Activities]] that can be embedded within other activities.
# Boilerplate
### Java File
```java
package com.safetyapp.mainapp;  
  
import android.os.Bundle;  
  
import androidx.fragment.app.Fragment;  
import android.view.LayoutInflater;  
import android.view.View;  
import android.view.ViewGroup;  
  
public class MenuFragment extends Fragment {  
  
    public MenuFragment() {  
    }  
  
    public static MenuFragment newInstance() {  
        MenuFragment fragment = new MenuFragment();  
        return fragment;  
    }  
  
    @Override  
    public void onCreate(Bundle savedInstanceState) {  
        super.onCreate(savedInstanceState);  
    }  
  
    @Override  
    public View onCreateView(LayoutInflater inflater, ViewGroup container,  
                             Bundle savedInstanceState) {  
        // Inflate the layout for this fragment  
        return inflater.inflate(R.layout.example_fragment, container, false);  
    }  
}
```
### Routing Java File
```java
package com.safetyapp.mainapp;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentTransaction;

public class HomeActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.home_activity);
        setTitle("Home Activity");
        Fragment myfragment = new MenuFragment();
        getSupportFragmentManager().beginTransaction().replace(R.id.fragment_box, myfragment).setTransition(FragmentTransaction.TRANSIT_FRAGMENT_OPEN).commit();
    }
}

```
### XML File
This can just be a regular [[Android Screen Layout|Layout]] file.