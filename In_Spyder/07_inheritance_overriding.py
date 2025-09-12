# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 19:02:59 2025

@author: BIMAL
"""

class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone constructor")
        self.price = price 
        self.__brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")



class SmartPhone(Phone):
    
    def buy(self):
        print("Buying a smartphone from SmartPhone class")

s= SmartPhone(20000,"Samsung","64MP")
s.buy()
# Child class can not access the private members of the parent class
# print(s.__brand)