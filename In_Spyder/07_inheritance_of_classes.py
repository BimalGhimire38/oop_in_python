# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 18:26:40 2025

@author: BIMAL
"""

class User:
    
    def login(self):
        print("Login")
        
    def register(self):
        print("register")
        
class Student(User):
    
    def enroll(self):
        print("Enroll")
        
    def review(self):
        print("Review")
        
        
        
s1 = Student()

s1.enroll()
s1.review()
s1.login()
s1.register()
    
    
    
    