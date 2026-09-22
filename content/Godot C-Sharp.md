---
tags:
  - programming
  - csharp
  - godot
aliases:
  - Godot C#
---
# Installation
```bash
sudo pacman -S godot-mono dotnet-sdk dotnet-runtime
```
# Concepts
- [[Godot C-Sharp Printing to Output]]
- [[Godot C-Sharp Export]]
- [[Godot C-Sharp Connecting Events]]
- [[Godot C-Sharp Assert]]
- [[Godot C-Sharp Autoload]]
# Boilerplate
```c#

public partial class MyClass : Node {

	[Export] private Node MyGuts {get; set;}
	
	public override void _Ready() {
	
	}
	
	public override void _Process(double delta) {
	
	}
}
```