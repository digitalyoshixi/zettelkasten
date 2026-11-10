---
tags:
  - programming
  - csharp
aliases:
  - C-Sharp String Length
  - C-Sharp String Uppercase
  - C-Sharp String Lowercase
  - C-Sharp Substring
---
C-Strings can be represented as [[C-Sharp Array]] of characters.
```cs
string mystr = "Hello";
Console.WriteLine(mystr[0]); // "H"
```
# Index of Character
```cs
string myString = "Hello";
Console.WriteLine(myString.IndexOf("e")); // 1
```
# Substrings
```cs
string original = "Who What When";
string middleToEnd = original.Substring(4); // What When
string middle = original.Substring(4, 4); // What (First argument position, second argument length)
```
# String Length
```cs
string txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
Console.WriteLine(txt.Length);
```
# String ToUpper()
```cs
string txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
Console.WriteLine(txt.ToUpper());
```
# String ToLower()
```cs
string txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
Console.WriteLine(txt.ToLower());
```
