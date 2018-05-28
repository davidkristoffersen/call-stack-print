#!/usr/bin/env python3

import tree

class A():
    def __str__(self):
        return 'Print of class'

def func1():
    print("Mid", 'Arg2', 'Arg3\nArg3.5')
    func2()
    dic = {'Key 0\n0.5': 0, 'Key 1': 1, 'Key 2': 2}
    print(dic)
    func6()
    print(A())

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

assert 4 == 2
if __name__ == "__main__":
    tree.enable(globals())
    func1()
