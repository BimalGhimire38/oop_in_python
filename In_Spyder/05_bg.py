# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 16:33:13 2025

@author: BIMAL
"""

class Customer:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def intro(self):
        print("I am ", self.name, " and I am ", self.age)
        
c1 = Customer("Bimal",21)
c2 = Customer("Bigyan",23)
c3 = Customer("Bhuwan",22)


L = [c1,c2,c3]

for i in L:
    i.intro()
    