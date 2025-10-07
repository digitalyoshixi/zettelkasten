---
tags:
  - python
---
A python library that allows python files to be ran with arguments easily.
# Installation
```
pip install typer
```
# Boilerplate main.py
```python
import typer
app = typer.Typer()

@app.command()
def hello(name: str):
    print(f"Hello {name}")

@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")

if __name__ == "__main__":
    app()
```
# Running with Typer
```
python main.py hello
```
# Typer Help Commands
```
python main.py --help
```