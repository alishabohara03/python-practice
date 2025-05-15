#6. Write a program to mine a log file and find out whether it contains 'python'.
with open("log.txt", "r") as f:
    content = f.read()

if "python" in content.lower():
    print("Yes, 'python' is present in the log file.")
else:
    print("'python' is not found in the log file.")
