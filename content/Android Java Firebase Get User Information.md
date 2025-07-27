---
tags:
  - android
  - database
---
# Boilerplate
```java

import com.google.firebase.auth.FirebaseAuth;

public MyClass(){

	private FirebaseAuth mAuth;
	private FirebaseUser localuser;

	public static void main(){
		this.mAuth = FirebaseAuth.getInstance();
		// lets try and get the userID
		try{
		    this.localuser = mAuth.getCurrentUser();
		    Log.d("CURRENT USER:", localuser.toString());
		}
		catch (Exception e){
		    System.err.println("YOU ARE NOT AUTHENTICATED");
		}
	}
	
}

```