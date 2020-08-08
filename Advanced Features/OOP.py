# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:49:33 2020

@author: LvGJ
"""


class Student(object):
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        
    def detail(self):
        print(self.name,":",self.grade)
        
s1 = Student("hyt",100)
s2 = Student("zz",90)


class Student2(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    
    def get_gender(self):
        return self.__gender
    
    def set_gender(self,gender):
        self.__gender = gender

class Screen(object):
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,w):
        self._width = w
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,h):
        self._height = h
        
    @property
    def resolution(self):
        return self._width*self._height





















