class Atm:
    __counter = 1
    
    def __init__(self):
        self.__pin = ""
        self.__balance =0
        self.sno = Atm.__counter
        Atm.__counter += 1
    @staticmethod
    def get_counter():
        return Atm.__counter
    @staticmethod
    def set_counter(new):
        if type(new)==int:
            Atm.__counter = new
            
        else:
            print("Not ALlowed")
  