#2. Write a class “Calculator” capable of finding square, cube, and square root of a number.
import math

class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        return self.num ** 2

    def cube(self):
        return self.num ** 3

    def squareRoot(self):
        return math.sqrt(self.num)


# Example usage
calc = Calculator(9)
print("Square:", calc.square())
print("Cube:", calc.cube())
print("Square Root:", calc.squareRoot())
