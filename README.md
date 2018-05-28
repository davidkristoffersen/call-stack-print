# call_stack_print
[![Build Status](https://travis-ci.org/davidkristoffersen/call_stack_print.svg?branch=master)](https://travis-ci.org/davidkristoffersen/call_stack_print)

## How to use

In a python file:

```python
import tree
```

At the start of your main function:

```python
tree.enable(globals())
```
