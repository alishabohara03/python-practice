#1. Find the Greatest of Four Numbers

# Input four numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

# Compare the numbers using nested if-else
greatest = max(a, b, c, d)

print("The greatest number is:", greatest)
