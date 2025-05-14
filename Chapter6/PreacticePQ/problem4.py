#Write a program to check if a username contains less than 10 characters.

# Input username
username = input("Enter your username: ")

# Check length
if len(username) < 10:
    print("Username is valid (less than 10 characters).")
else:
    print("Username is too long.")
