class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone constructor")
        self.__price = price 
        self.brand = brand
        self.camera = camera
        
    def buy(self):
        print("Buying a Phone")
        
class SmartPhone(Phone):
    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera)
        self.os = os
        self.ram = ram
        
s = SmartPhone(20000,"Samsung","48 MP","Android",8)

print(s.os)
print(s.brand)