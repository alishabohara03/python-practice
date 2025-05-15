class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000


Alisha = Employee()
Alisha.language = "JavaScript" # This is an instance attribute
print(Alisha.language,Alisha.salary)