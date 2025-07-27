---
tags:
  - database
  - android
aliases:
---
# Boilerplate
```java
import com.google.firebase.database.DatabaseReference;  
import com.google.firebase.database.FirebaseDatabase;


private DatabaseReference dbRef;
public Myclass{
	this.dbRef = FirebaseDatabase.getInstance().getReference();
	String mytempdata = "HELLO";
	dbRef.child("myroute").setValue(mytempdata);
}
```