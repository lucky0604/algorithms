#!/usr/bin/env python3
#-*- coding: utf-8 -*-
'''
write an algorithm that will read a string of parentheses from left to
right and decide whether the symbols are balanced.
(((())))        balanced
(((())          not balanced
'''
# import the Stack class
from Stack import Stack

def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False

print(par_checker('((()))'))            # True
print(par_checker('((())'))             # False
