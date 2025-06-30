---
tags:
  - android
  - software
---
# Activity
Responsible for user interaction with the screen. Written in [[Java]].
Activities can use one or more fragments.
![[Android Screen Activity-20250623213300357.webp|359]]
# Location
`/app/java/com.example.*/*`
![[Android Screen Activity-20250630154710537.webp]]
# Boilerplate
```java
package com.gfg.myapplication;

import android.os.Bundle;
import android.widget.Button;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button button = findViewById(R.id.button1);
        EditText editText1 = findViewById(R.id.editText1);

        button.setOnClickListener(new View.OnClickListener(){
           @Override
           public void onClick(View v){
               String text = editText1.getText().toString();

               Toast.makeText(MainActivity.this, text, Toast.LENGTH_SHORT).show();

           }
        });

    }
}
```