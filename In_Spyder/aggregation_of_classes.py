# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 18:07:49 2025

@author: BIMAL
"""

class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
        
        
    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name = new_name
        self.address.change_address(new_city,new_pin,new_state)
        
        
class Address:
    def __init__(self,city,pincode,state):
        self.city = city
        self.pincode=pincode
        self.state=state
        
    def change_address(self,new_city,new_pincode,new_state):
        self.city = new_city
        self.pincode = new_pincode
        self.state = new_state
        
add = Address("Lalitpur",44200,"Bagmati")
cust = Customer("Bimal","male",add)

cust.edit_profile("Rachana","Kathmandu",44000,"Karnali")


print(cust.name)







