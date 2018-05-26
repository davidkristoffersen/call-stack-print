#!/usr/bin/env python3

from .config import *

class Tree():
    def __init__(self):
        # Call stack is pushed to this array
        self.stack = []
        # Used in the call tree print
        self.type = type_mid

        self.enter_str = enter_str if print_unicode else "<"
        self.mid_str = mid_str if print_unicode else "|"
        self.connect_str = connect_str if print_unicode else "K"
        self.exit_str = exit_str if print_unicode else ">"
        self.padd_str = padd_str if print_unicode else "-"

    # Push'ing function to call stack
    def push(self, func):
        self.stack.append(func)
        self.type = type_enter
        self.out('')
        self.type = type_mid

    # Pop'ing function to call stack
    def pop(self):
        self.type = type_exit
        self.out('')
        self.stack.pop()
        self.type = type_mid

    def out(self, *args):
        if print_tree:
            self.out_internal(*args)

    def out_internal(self, *args):
        print(col_faint + "{:2}".format(hex(len(self.stack) - 1)[2:]), end='')

        for i in range(len(self.stack) - 1):
            print(self.mid_str + " " * padd_width, end='')

        if self.type == type_enter:
            print(col_green + self.enter_str, end='')
        elif self.type == type_exit:
            print(col_red + self.exit_str, end='')
        else:
            print(self.connect_str, end='')
        print(self.padd_str * padd_width, end='')

        if not self.type == type_mid:
            print(col_bold + col_brown + self.stack[-1], end='')
            print(col_reset)

        if self.type == type_mid:
            print(col_reset + col_faint, end='')

            padd_sub = len(self.stack) * (padd_width + 1)
            for i in range(padd_len - padd_sub):
                print(self.padd_str, end='')
            print(col_reset, end=' ')

            print(*args)
