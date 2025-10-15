class Phone:
    def __init(self,price,brand,camera):
        print("Inside Phone constructor")
        self.__price = price 
        self.brand = brand
        self.camera = camera
        
    def buy(self):
        print("Buying a Phone")
        
class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")
        super().buy()
        
s = SmartPhone(20000,"Samsung","48 MP")
s.buy()