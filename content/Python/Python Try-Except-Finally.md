---
tags:
  - python
  - programming
---
Often times we have errors in our programs. When we get an error, our program crashes. This may happen sometimes unexpectedly, and there is no way around it. In these cases, we must use a few methods to catch these errors and prevent our program from dying.

  

**Try:** try a snippet of code. It it doesn’t work move to exceptions

**except:** catches the error resulted from the code from the try segment. Runs another piece of code reactionary.

**Finally:** executes some code regardless of the previous error/non-error state.

  

[https://www.youtube.com/watch?v=brICUKrzVR0&t=5s](https://www.youtube.com/watch?v=brICUKrzVR0&t=5s)

he will tell us some exceptions.

In his code, he will have the following error when attempting to divide by 0:![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivuq_tmp_335111fe60b219bf.png)

he gets the ZeroDivisionError. This is an error that we can catch.

Depending on the type of error, we can get a different exception code. ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivuq_tmp_b8f74c5fb761bfa9.png) 

  

our try and except will look like this:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivuq_tmp_643e9488f60561ac.png)

if an exception occurs in the try block, then the code executor immediately jumps to the except block where the code continues executing.

  

### Difference between except and catch

Catch will only catch specific exception codes, except will catch all exceptions.

Below is an example of a catch:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivuq_tmp_7bcd9d252c508748.png)

it will only except if the error above is the ZeroDivisionError exception.

You can have multiple catches as well:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivuq_tmp_76c63e319af3ba18.png)

  

[https://stackoverflow.com/questions/11551996/why-do-we-need-the-finally-clause-in-python](https://stackoverflow.com/questions/11551996/why-do-we-need-the-finally-clause-in-python)

the finally block is optional, its very useful for cleanup like closing files because it gets run regardless of program behavior. It is literally one of the very few lines of code that always runs.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivuq_tmp_dbf34f11e19f3f4b.png)

no matter if there is a unforeseen catch, or secondary error, finally will always run.