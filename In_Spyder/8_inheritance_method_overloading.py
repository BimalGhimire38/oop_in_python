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
    def show(self):
        print("This is in child class")
        
son = Child(100)
print(son.get_num())
son.show()



