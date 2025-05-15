class Employee:
    # Class attributes
    language = "Python"
    salary = 1200000

    # Constructor with default values
    def __init__(self, name="John Doe", salary=50000, language="Python"):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    # Instance method
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    # Static method
    @staticmethod
    def greet():
        print("Good morning")


# Creating an employee with custom values
alisha = Employee("Alisha", 1300000, "JavaScript")
print(alisha.name, alisha.salary, alisha.language)

# Creating an employee with default values
rohan = Employee()
print(rohan.name, rohan.salary, rohan.language)
