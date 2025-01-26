---
tags:
  - programming
  - java
---
tries a block of code taste tests! if it is good, then we are find, it executed, we are ok.
If it fails, it goes to the catch block.
```
try{
	//some block of code
}
catch (IOException e){
	System.out.println(e);
}
catch (FileNotFoundException e){
	System.out.println(e);
}
finally{
	// do some shit
}
```
