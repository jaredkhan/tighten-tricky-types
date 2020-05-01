# Top tips to tighten tricky types

A few examples of how to make your function signatures more specific in Python.
Each example has some function, with a before and an after.
The implementation of the function won't change between the before and after, but the types will!

Running `mypy` on the examples, we will see that being more specific about our types 
can prevent invalid usages of functions before the code is even run.

To run the examples:
```bash
virtualenv venv -p python3.8
source venv/bin/activate
pip install mypy
mypy 1-polymorphism/before.py
...
```
