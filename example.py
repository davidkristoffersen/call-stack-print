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
