#3. Create a class with a class attribute a; create an object from it and set a directly using object.a = 0. Does this change the class attribute?

class Sample:
    a = 5

obj = Sample()
print("Before changing:", Sample.a)

obj.a = 0  # creates instance attribute, doesn't change class attribute
print("obj.a:", obj.a)
print("Sample.a:", Sample.a)  # still 5
