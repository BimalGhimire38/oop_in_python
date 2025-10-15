# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 20:56:30 2025

@author: BIMAL
"""

# 2082/06/29  10:41 AM, @ Home, Bidhyapur

class Parent:
    def __init__(self, num):
        self.__num = num
        
    def get_num(self):
        return self.__num
    
class Child(Parent):
    def __init__(self,val,num):
        self.__val=val
    def get_val(self):
        return self.__val
        
son = Child(100,200)
print("Parent Num",son.get_num())
print("Child val",son.get_val())



