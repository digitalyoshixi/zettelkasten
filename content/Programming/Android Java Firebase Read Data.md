---
tags:
  - java
  - android
  - database
---
# Read Data Once Boilerplate
```java
private DatabaseReference mDatabase;
// ...
mDatabase = FirebaseDatabase.getInstance().getReference();

mDatabase.child("users").child(userId).get().addOnCompleteListener(new OnCompleteListener<DataSnapshot>() {
    @Override
    public void onComplete(@NonNull Task<DataSnapshot> task) {
        if (!task.isSuccessful()) {
            Log.e("firebase", "Error getting data", task.getException());
        }
        else {
            Log.d("firebase", String.valueOf(task.getResult().getValue()));
        }
    }
});
```