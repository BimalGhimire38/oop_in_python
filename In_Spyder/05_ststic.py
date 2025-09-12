class Atm:
    
    # Magic Methods in Python (__magic_method_name__)
    
    # __init__ method is a special method in python class
    # it is called a constructor and is automatically called when an object of the class is created
    
    # Instance Variable are those variable whose value is different for different object
    
    # static/class variable
    counter = 1
    
    def __init__(self):
        self.__pin = ""
        self.__balance =0
        self.sno = Atm.counter
        Atm.counter += 1
    def get_pin(self):
        return self.__pin
    def set_pin(self,new_pin):
        if type(new_pin) ==str:
            self.__pin =new_pin
            print("Pin Changed")
        else:
            print("Not allowed")
    def menu(self):
        user_input = input('''0
                           Hello, How would you like to proceed?
                           1. Enter 1 to create PIN
                           2. Enter 2 to deposit 
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
                           ''')
        if user_input=='1':
            self.create_pin()

        elif user_input=='2':
            # print("Deposit")
            self.deposit()

        elif  user_input=='3':
            self.withdraw()

        elif user_input=='4':
            self.check_balance()

        else:
            print("Exit")

    def create_pin(self):
        self.__pin = input("Enter Your PIN")
        print("Pin Set Successfully")
    def deposit(self):
        temp = input("Enter your PIN: ")
        if temp==self.__pin:
            amount = int(input("Enter the anmount to deposit : "))
            self.__balance+=amount
            print("Deposit Successfully")

    def withdraw(self):
        temp = input("Enter your PIN: ")
        if temp==self.__pin:
            amount = int(input("Enter the anmount to withdraw : "))

            if amount<=self.balance:
                self.__balance -=amount
                print("Withdrawn Successfully")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid PIN")

    def check_balance(self):
        temp = input("Enter your PIN: ")
        if temp==self.__pin:
            print(f"Your balance is {self.__balance}")
    


b = Atm()
