#4. Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        return self.num ** 2

    def cube(self):
        return self.num ** 3

    def squareRoot(self):
        return self.num ** 0.5

    @staticmethod
    def greet():
        print("Hello User!")


# Example usage
Calculator.greet()
calc = Calculator(4)
print("Cube:", calc.cube())
