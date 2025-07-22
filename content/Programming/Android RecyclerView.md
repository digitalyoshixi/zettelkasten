---
tags:
  - android
---
```java
package com.safetyapp.mainapp;

import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class QuestionaireAdapter extends RecyclerView.Adapter<QuestionaireAdapter.MyViewHolder>{

	// inflating the layout with items
    @NonNull
    @Override
    public QuestionaireAdapter.MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        return null;
    }

	// setting data within a view, based off position in recycler view
    @Override
    public void onBindViewHolder(@NonNull QuestionaireAdapter.MyViewHolder holder, int position) {

    }
    
	// get the total number of views
    @Override
    public int getItemCount() {
        return 0;
    }

	// assigning all view to a variable (like oncreate method)
    public static class MyViewHolder extends RecyclerView.ViewHolder{

        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
        }
    }
}
```