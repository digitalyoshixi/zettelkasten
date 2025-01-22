---
tags:
  - nix
---
Creating a function name to be called with a given number of inputs
![[Nix Function-20240828012500347.webp]]
It is advised to combine them with [[Nix Let]] so that they are evaluated within [[NixOS]] configuration files.
![[Nix Function-20240828012725371.webp]]
# Nesting Functions
Functions are nested by default. What this means is that, if you provide multiple inputs, there will be other functions created that carry and separate the inputs so that they can be evaluated separately.
![[Nix Function-20240828012840381.webp]]
If you want to avoid nesting, pass parameters as sets
# Sets as Parameters
![[Nix Function-20240828013241023.webp]]
This is very similar to configuration.nix, where inputs are recieved and the body is evaluated.
![[Nix Function-20240828013337221.webp|591]]
# Default Attributes
You can set default values for attributes incase a value is not given
![[Nix Function-20240828013602024.webp]]
# Ignoring Additional Arguments
Use an ellipsis to note that only 2 inputs are required.
![[Nix Function-20240828013700626.webp]]
# Saving All Parameters
Use `@<variablename>` to save all parameters to variable `<variablename>`
![[Nix Function-20240828013819691.webp]]
