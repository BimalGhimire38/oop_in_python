# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 14:59:48 2025

@author: BIMAL
"""

#class Customer:
#     def __init__(self,name):
#         self.name = name
        
# def greet(customer):
#     print(id(customer))
#     customer.name = "Ghimire"
#     print(customer.name)
#     print(id(customer))
# cust = Customer("Bimala")
# #print(id(cust))
# print(cust.name)
# greet(cust)
# print(cust.name)
# # These two variable will point to the same memory location



def change(L):
    print(id(L))
    L.append(4)
    print(id(L))

l1 = list([1,2,3])
print(id(l1))
change(l1[:])

print(l1)




