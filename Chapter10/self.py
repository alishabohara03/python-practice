

class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


Alisha = Employee()
# Alisha language = "JavaScript" # This is an instance attribute
Alisha.greet()
Alisha.getInfo() 
# Employee.getInfo(Alisha)