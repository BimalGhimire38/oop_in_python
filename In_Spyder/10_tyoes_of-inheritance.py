# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 16:11:45 2025

@author: BIMAL
"""

class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
        
    def buy(self):
        print("Buying a Phone")
        
class Product:
    def buy(self):
        print("Product buy method")
        
class SmartPhone(Product,Phone):
    def smph(self):
        return 0

s = SmartPhone(15000, "Samsung", 12)

s.buy()