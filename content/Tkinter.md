---
tags:
  - python
---
A graphics library for python to build GUI apps.
# Boilerplate
```python
import tkinter as tk

window = tk.Tk()

lbl = tk.Label(window, text="hello")
keep = tk.Button(window, text="keep")
keep.grid(column=1, row=1)
toss = tk.Button(window, text="toss")
toss.grid(column=2, row=1)
window.mainloop()
```