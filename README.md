# call_stack_print

[![Build Status](https://travis-ci.org/davidkristoffersen/call_stack_print.svg?branch=master)](https://travis-ci.org/davidkristoffersen/call_stack_print/builds)
[![HitCount](http://hits.dwyl.io/davidkristoffersen/call_stack_print.svg)](http://hits.dwyl.io/davidkristoffersen/call_stack_print)
![badge](https://img.shields.io/badge/implemented-yes-brightgreen.svg?style=flat)

## How to use

In a python file:

```python
import tree
```

At the start of your main function:

```python
tree.enable(globals())
```
