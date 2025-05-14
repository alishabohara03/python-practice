#Write a program to find out whether a student has passed or failed.

# Input marks of 3 subjects
sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))

# Calculate average
average = (sub1 + sub2 + sub3) / 3

# Check pass conditions
if sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and average >= 40:
    print("You have passed!")
else:
    print("You have failed.")
