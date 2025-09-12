# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 14:59:48 2025

@author: BIMAL
"""

class Customer:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        
def greet(customer):
    if customer.gender == "Male":
        print("Hello",customer.name, "Sir")
        
    else:
        print("Hello",customer.name, "Ma'am")
        
    cust2 = Customer("BIMALA","Female")
    return cust2

        
        
cust = Customer("Bimal", "Male")
new_cust = greet(cust)
print(new_cust.name)