![version number](https://badge.fury.io/py/guizero.svg)

# guizero (COMP490 Project 2)

[guizero](https://lawsie.github.io/guizero) is a Python 3 library for creating simple GUIs.

This fork was created for the COMP490 Senior Capstone Project 2. 

You can find more information on the project [here](https://webhost.bridgew.edu/jsantore/Spring2021/Capstone/Project2assignment.html).

![Have a go with guizero and see what you can create](docs-src/docs/images/have-a-go.png)

```python
from guizero import App, Text, PushButton

app = App(title="guizero")

intro = Text(app, text="Have a go with guizero and see what you can create.")
ok = PushButton(app, text="Ok")

app.display()
```

## Install

If you can download and unzip a file, you can [install guizero](https://lawsie.github.io/guizero/#easy-install) - **no special permissions or administrator rights are required**.

The "guizero" folder goes into the project directory of your Python app.

## External Documentation

Comprehensive documentation (for the original guizero) can be found at [lawsie.github.io/guizero](https://lawsie.github.io/guizero) including:
+ [installation instructions](https://lawsie.github.io/guizero)
+ [a getting started guide](https://lawsie.github.io/guizero/start)
+ [recipes](https://lawsie.github.io/guizero/recipes)
+ [an API reference](https://lawsie.github.io/guizero/app/)

## Aims
The aim of guizero is to make the process of creating simple GUIs quick, accessible and understandable for new learners.

* Works with standard Python Tkinter GUI library (and no need to install other libraries)
* Abstracts away details new learners find difficult to understand (such as Tkinter StringVar() objects)
* Accessible widget naming system to help new learners to build up a mental model
* Flexible enough to be used for projects up to A-Level standard, yet accessible to primary school children
* Comprehensive and accessible documentation with examples
* Generates helpful additional error messages

The aim of our fork is to fix some of the 22 issues listed on the original project page.