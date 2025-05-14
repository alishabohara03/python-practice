# Write a program to calculate the grade of a student based on marks.
# Grade Scheme:

# 90–100 => Ex

# 80–90 => A

# 70–80 => B

# 60–70 => C

# 50–60 => D

# <50 => F


# Input marks
marks = float(input("Enter your marks (0-100): "))

# Determine grade
if marks >= 90 and marks <= 100:
    grade = "Ex"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)







