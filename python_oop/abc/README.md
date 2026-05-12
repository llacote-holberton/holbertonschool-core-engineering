# Overview

This directory holds tasks tailored to learn about class inheritance mechanisms.

# General Rules
- Corrections will run on Ubuntu 20.04 LTS.
- Python version used for correction: Python 3.8.x.
- Every Python file must start exactly with:  
  `#!/usr/bin/env python3`
- Every Python file must:
  * End with a newline.
  * Be PEP8 compliant (pycodestyle 2.7.x).
  * All modules, classes, and functions must include documentation strings.
  * Only the Python standard library may be used unless otherwise stated.
  * Do not use the words import or from inside your comments,  
    the checker will think you are trying to import some modules.
  * To import any base class use the __import__method.
  * All scripts must behave exactly as specified in the task instructions.

# Exercises

| Task name                                                     | Filename          |
|---------------------------------------------------------------|-------------------|
| 0. Abstract Animal Class and its Subclasses                   | animals.py        |
| 1. Shapes, Interfaces, and Duck Typing                        | shapes.py         |
| 2. The Enigmatic FlyingFish - Exploring Multiple Inheritance  | flyingfish.py     |
| 3. The Mystical Dragon - Mastering Mixins                     | dragon.py         |
| 4. Extending the Python List                                  | verboselist.py    |
| 5. Final Quizz                                                | (quizz)           | 

# Notes

## Duck Typing

In Python, objects are often used based on what they can do, not only on what they inherit from.

Example idea:
* if an object provides a method named draw(), it may be usable in a function that expects something drawable
* the object does not always need to inherit from a specific class for that use case

  This approach is often called duck typing.
