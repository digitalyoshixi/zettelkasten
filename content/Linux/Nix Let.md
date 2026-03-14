---
tags:
  - nix
---
A method to evaluate a snippet of code explicitly.
Useful in [[NixOS]] configuration files, where the code is only evaluated once, using 'let' statements, allows for multiple evaluations per file.
```c
let
	my-var = {
		one - "hello";
		two = "world";
	}
in 
my-var.one
```
These expressions are parsed recursively until all values are evaluated.
[[Nix Rec]] is let, but it evaluated within the same [[Nix Attribute Set]]