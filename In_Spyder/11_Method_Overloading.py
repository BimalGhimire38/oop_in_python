# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 16:31:48 2025

@author: BIMAL
"""

class Geometry:

    def area(self,a,b=0):
        if b==0:
            print("Circle",3.14*a*a)
            
        else:
            print("Rectangle",a*b)
    
obj = Geometry()
obj.area(2)
obj.area(2,3)