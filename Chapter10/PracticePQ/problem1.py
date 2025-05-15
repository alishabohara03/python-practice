#1. Create a Class “Programmer” for storing information of few programmers working at Microsoft.



class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"Name: {self.name}, Product: {self.product}, Company: {Programmer.company}")


# Example usage
p1 = Programmer("Alice", "VS Code")
p2 = Programmer("Bob", "GitHub")

p1.getInfo()
p2.getInfo()
