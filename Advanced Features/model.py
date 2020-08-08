# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:42:36 2020

@author: LvGJ
"""
'a test moudle'
__author__='LvGJ'


def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

if __name__ == '__main__':
    print(greeting("hello"))