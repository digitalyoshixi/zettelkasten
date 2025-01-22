---
tags:
  - programming
aliases:
  - OOP
---
OOP is about representing real world objects as computerized models called classes.

A class is a template or type and an object is an instance of that class/type.

When you make a class, you are making a type like bool, int, etc, but you name it something else.

You can give a class any atrribute you desire. Like a health value, a dmg value, a name value, all of these are attributes in the class which are made of different data types.

  

### Instantiation

Making an object from a class is called instantiation. Do you see it? INSTANCE. INSTANTIATON! You make an instance from a class.

  

### Python class creation and instantiation

We are going to use python to do OOP.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_bb0bcddc78c6b76.png)

this script is to create dog classes.

We are making a datatype DOG.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_888aba8182091f6c.png)

and then we have a __init__ method for constructing the class.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_33eef1368343cc97.png)

so, when you instantiate, you will give it 2 arguments. The name argument and the age argument.

And we are going to make those atrributes relative to the dog.

Dog will have a name and an age.

Ok, then we have a sit method. This will just print out something very simply cause we are too bored to actually make a dog.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_231aa1bd15c61ac8.png)

this is a method that just needs to be called. No arguments needed to be fed into it. We print our dog name and we say that it is sitting down.

Afterwards we instantiate into a variable.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_f0a9ce5149d79886.png)

and then we print the type out just to prove that we have made our own datatype.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_e4c02c7b80e20b10.png)

and lastly, we will run our method we just made.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_b6f3c9cf9176d1f5.png)

so the final output is this:  
![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_1ececca737c98102.png)

  

there is also, and this is sidetracking a bit, but there is also a .title() function in python that just captializes the first letter in a string. So, abbey → Abbey. Just do .title() after a string.

  

### Functions vs methods:

Functions and methods are both very similar and can be used interchangably for the most part, but a method is usually used when talking about object-oriented programming. However, since a method is associated with an object, a method run will implicitly take the self argument as the object it was used on.

Remember, all methods have a self parameter for the first one. This one is implicitly called everytime for with different objects being the ‘self’.

The class is the definition, an object is just an instance of that data.

[https://stackoverflow.com/questions/155609/whats-the-difference-between-a-method-and-a-function](https://stackoverflow.com/questions/155609/whats-the-difference-between-a-method-and-a-function)

  

right, so I also wanted to experiment with default parameters since I remember it is possible.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_bdeb0cd3b06ee37a.png)

yes, I tried it out, and this works. You can give default values to arguments if they were not given beforehand.

  

### __init__ method:

The __init__ method is called automatically when instantiation takes place. It is the constructor. The reason why there are double underscores on each side is to prevent python’s default method names from clashing with your own method names. Again, this is a method so you will always pass self as the first parameter of this method.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_8ef299fa7aaa22c4.png)

its also advised to use the constructor to lay out the attributes of this object. Make all your traits inside the constructor.

  

### Attributes

An attribute is a variable special to each object

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_6676b083be2497e0.png)

you just do self.attributename = value

very simple. And you can modify this value later on in your class methods or for current instance manipulation.

  

### Callable classes

For some reason, a class is also callable. So if you instantiate a class and then just call it like a function, you can actually return or modify values.

Don’t know why anybody would use this, but it exists.

To do this, just do __call__ as a method in the function.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_93839742995622a9.png)

and then I just call the object directly

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_6401ef6a4e795aa8.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_8906ff4babbd0aaa.png) ’

  

### Class inheritance

So, if you did some experimenting, you may realize that we can make a class without the parenthesis.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_8e9b8c6be56ab85a.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_7eecc5a03bc7e698.png)

both of these do the exact same thing, only due to the fact that there is nothing inside the parenthesis of the second declarator.

Now, if there was something inside those parenthesis, we would be able to inherit.

So, assume we have 2 classes here. One is for the class dog, the other is for the class cat.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_2d12a5499d8e60da.png)

now, what you will notice is that cat and dog are pretty much the same, except for the fact that the speak method prints out different strings. They are almost identical. Now, the idea behind inheritance is that if you have several similar classes, instead of writing the same class twice, you can acutally inherit from an upper-level class like boilerplate. What we can inherit is the __init__ method here, because that is the method that is the one that is being repeated.

So, how we make an upperlevel class is this:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_601c4db47a155296.png)

so this is our upper level class.

They will also inherit the show method from this Pet class as well.

Lets try that out.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_4e2c078d15ebfd6.png)

an inheritance is simply just adding brackets after the class with the inherit parent after it

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_5f8ffb86b7c8b94e.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_af3fe3b2af9feacd.png)  
for real!

Now, an important thing to note is that if you redefine a method in a lower-level child class, that method will override whatever method is in the upper-level parent class.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_ac9a5abcaf41c53c.png)

see above that the cat class is redefining the speak method. And now, then we instantiate and then run the speak method for both pet and cat instances these are the results:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_e175d3b06812f618.png)

you can also just make the most useless pet in the world that is 100% boilerplate

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_7a0247cbf2c8c727.png)

just put a pass after the declarator

  

now, say that we want to change our __init__ method to have new attributes.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_e0dd5585abfb7988.png)

the above code cannot slide. We cannot let this slide. Not on my watch, hell no.

we have 2 options:

1. manually do self.name = name; self.age = age
    
2. do a super().__init__(name, age)
    
    ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw60_tmp_25ac568d3f710fd9.png)
    

what super does is it references the super class which in our case is the Pet class. __init__ finds the method we want to call. And then name, age. It will run the lines in the initialization that assign values to name and age.