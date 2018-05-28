#!/usr/bin/env python3

"""
tree.py
tree module.
Contains decorator functions for printing an UNIX tree like function enter and exit
"""

__author__  = "David Kristoffersen"
__email__   = "david.alta2010@gmail.com"

from .config import *
from .classes import Tree

print(htfeihtei)

def decorator(func):
    def wrapper(*args, **kwargs):
        tree.push(str(func.__name__))
        ret = func(*args, **kwargs)
        tree.pop()

        return ret
    return wrapper

def enable(glob):
    for key, val in get_functions(glob).items():
        deco_function(glob, key, val)
    if print_polymorph:
        glob['print'] = poly_out

def poly_out(*args, **kwargs):
    tree.out(*args, **kwargs)

def get_functions(glob):
    return {key: val for key, val in glob.items() if callable(val)}

def deco_function(glob, key, val):
    try:
        glob[key] = decorator(val)
    except Exception:
        print("Function not found in globals")

tree = Tree()

if __name__ == "__main__":
    raise NotImplementedError(__file__ + " does not support to be run as main!")
