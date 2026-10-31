---
tags:
  - programming
  - csharp
aliases:
  - C-Sharp Method
---
```cs
static void MyMethod(){
	// ..
	return 20;
}

MyMethod();
```
# Function With Parameters
```cs
static void MyMethod(string arg = "damien", int arg2 = 0){
	// ..
	return arg + "-chan" + (string)arg2;
}

MyMethod("daniel");
MyMethod(arg : "david", arg2 : 2);
```
- Has default parameters "damien" and 4