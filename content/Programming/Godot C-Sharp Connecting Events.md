---
tags:
  - programming
  - godot
---
```cs
public override void _Ready()
{
    var button = GetNode<Button>("MyButton");
    // connect with += operator
    button.Pressed += OnButtonPressed;
}

private void OnButtonPressed()
{
    GD.Print("Button was pressed!");
}
```