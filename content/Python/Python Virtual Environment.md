---
tags:
  - python
aliases:
  - Python venv
  - venv
---
Creating an isolated environment of python packages independent from preexisting packages on the system.
It allows you to configure the:
- python interpreter
- software libraries
- binaries
to be specific version to support your python projects
# Installation
`pip install virtualenv`
# Creation
`python -m venv <directory>`
it makes a directory or populates a current directory with the basic files
![[Python Virtual Environment-20240701033613063.webp]]
`python -m venv venv` is the standard directory name
# Activate Virtual Environment
when you are inside of the directory,
##### [[Fish]]
`source bin/activate.fish`
##### [[Bash]]
`source bin/activate`
### [[Windows]]
`.\Scripts\activate`
To see if you are in a venv, type `pip list`
![[Python Virtual Environment-20240701040015591.webp]]
You should have `pip`, `wheel`, `setuptools`, `python-dotenv` installed. (If you dont, install them manually)
# Deactivate Virtual Environment
When in a venv, just type `deactivate` and then you will deactivate it
![[Python Virtual Environment-20240701040251762.webp]]
# Freezing Files
`pip freeze >> requirements.txt`
To install from requirements.txt, `pip install -r requirements.txt`