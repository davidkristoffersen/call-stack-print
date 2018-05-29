# call_stack_print

[![Build Status](https://travis-ci.org/davidkristoffersen/call_stack_print.svg?branch=master)](https://travis-ci.org/davidkristoffersen/call_stack_print/builds)
![HitCount](http://solnes.co/hits-badge/davidkristoffersen/call_count_print.svg)
<!-- ![badge](https://img.shields.io/badge/implemented-yes-brightgreen.svg?style=flat) -->

## How to use

In a python file:

```python
import tree
```

At the start of your main function:

```python
tree.enable(globals())
```

## Example

**Code:**

```python
#!/usr/bin/env python3

import tree

class A():
    def __init__(self):
        print("Init of class")
    def __str__(self):
        return 'Print of class'

def func0():
    print("Arg0", 'Arg1', 'Arg2')

    func1()

    dic = {'Key 0': 0, 'Key 1': 1, 'Key 2': 2}
    print(dic)

    func2()

    a = A()
    print(A())

def func1():
    print("Level 1")
    func2()

def func2():
    print("Level 2")

if __name__ == "__main__":
    tree.enable(globals())
    func0()
```

**Output:**

```
0
```
```diff
+┌──
```
```
func0
0 ├─────────────────────────────────────── Arg0 Arg1 Arg2
1 │  ┌──func1
1 │  ├──────────────────────────────────── Level 1
2 │  │  ┌──func2
2 │  │  ├───────────────────────────────── Level 2
2 │  │  └──func2
1 │  └──func1
0 ├─────────────────────────────────────── {'Key 0': 0, 'Key 1': 1, 'Key 2': 2}
1 │  ┌──func2
1 │  ├──────────────────────────────────── Level 2
1 │  └──func2
1 │  ┌──A
1 │  ├──────────────────────────────────── Init of class
1 │  └──A
1 │  ┌──A
1 │  ├──────────────────────────────────── Init of class
1 │  └──A
0 ├─────────────────────────────────────── Print of class
0 └──func0
```
