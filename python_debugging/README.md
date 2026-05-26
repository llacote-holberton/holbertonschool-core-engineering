# Overview

This repository holds provided and modified source for the Python - Debugging Strategies project
  which aims at presenting tools and tactics to efficiently find and fix root causes for most bugs.

# General Rules

## Python projects
- Corrections will run on Ubuntu 20.04 LTS.
- Python version used for correction: Python 3.8.x.
- Every Python file must start exactly with:  
  `#!/usr/bin/env python3`
- Every Python file must:
  * Be executable.
  * End with a newline.
  * Be PEP8 compliant (pycodestyle 2.7.x).
  * Output must match expected formatting exactly.
  * No external libraries are allowed unless explicitly requested.

# Exercises

Confer https://intranet.hbtn.io/projects/3864
All "fixed versions" of provided files will be the same name prefixed by task number.
Ex for T0 reading.py -> 0-reading.py
 
| Task name                                            | Original filename               |
|------------------------------------------------------|---------------------------------|
| 0. Reading the Bug                                   | reading.py                    |
| 1. Write to a file                                   | write_file.py                   |
| 2. Append to a file                                  | append_write.py                 |
| 3. Final quizz                                       | print_hexa.py                   |


# Resources

The following are recommended resources and tools

## Documentation
- Interpreter's User Guide: https://docs.python.org/3/tutorial/interpreter.html
- Components management: https://pip.pypa.io/en/stable/user_guide/
- Python virtual environments: https://docs.python.org/3/library/venv.html
- System object: https://docs.python.org/3/library/sys.html
- Builtin functions: https://docs.python.org/3/library/functions.html
- Builtin types: https://docs.python.org/3/library/stdtypes.html
- C to Python: https://docs.python.org/3/c-api/index.html

## Tools
- Online prototyper: https://pythontutor.com/visualize.html#
- Debugger tool: https://docs.python.org/3/library/pdb.html
- Codestyle checker: https://pypi.org/project/pycodestyle/
