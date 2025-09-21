class User:
    
    def login(self):
        print("Login")
        
    def register(self):
        print("Register")
        
        
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

        
        
        
        
        
        
        
        