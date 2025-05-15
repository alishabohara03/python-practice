#7. Write a program to find out the line number where 'python' is present (from question 6).


with open("log.txt", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "python" in line.lower():
        print(f"'python' found at line {i + 1}")
