#2. Write a program to input eight numbers from the user and display all the unique numbers (once).

numbers = set()
for _ in range(8):
    num = int(input("Enter a number: "))
    numbers.add(num)

print("Unique numbers are:", numbers)
