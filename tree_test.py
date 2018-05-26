#!/usr/bin/env python3

"""
tree_test.py
Tree module tester.
Contains tests for the tree module
"""

__author__  = "David Kristoffersen"
__email__   = "david.alta2010@gmail.com"

import tree

def func1():
    print("Mid")
    func2()
    func6()

def func2():
    print("Mid")
    func3()
    func4()

def func3():
    print("Mid")

def func4():
    print("Mid")
    func5()

def func5():
    print("Mid")

def func6():
    print("Mid")

if __name__ == "__main__":
    tree.enable(globals())
    func1()
