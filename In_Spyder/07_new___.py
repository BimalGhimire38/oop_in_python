# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 20:47:14 2025

@author: BIMAL
"""

class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
        
    def buy(self):
        print("Buying a Phone")
        
class SmartPhone(Phone):
    
    def buy(self):
        print("Buying a Smartphone")

s = SmartPhone(40000, "Samsung", "64 MP")
s.buy()

# Method Overriding --> Polymorphism
# Method Overloading
# Operatoe Overloading


