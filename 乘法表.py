# -*- coding: utf-8 -*-
"""

Created on 2018/2/11
@Author   ：QITINGSHE

"""
def w():
    """use WhileLoop to print"""
    i = 0
    while i < 9:
        i += 1
        j = 0
        while j < i:
            j += 1
            print('{}*{}={}'.format(j, i, j * i), end=" ")

        else:
            print('\n')


def f():
    """use ForLoop to print"""
    for i in range(9):
        i += 1
        for j in range(i):
            j += 1
            print('{}*{}={}'.format(j, i, j * i), end=" ")

        else:
            print('\n')


def pri(i, j):
    if j < i:
        j += 1
        print('{}*{}={}'.format(j, i, j * i), end=" ")
        if j < i:
            pri(i, j)
        else:
            print('\n')


def wif():
    """use WhileLoop and if-else to print"""
    i = 0
    while i < 9:
        i += 1
        j = 0
        pri(i, j)


def fif():
    """use ForLoop and if-else to print"""
    for i in range(9):
        i += 1
        j = 0
        pri(i, j)


fif()
