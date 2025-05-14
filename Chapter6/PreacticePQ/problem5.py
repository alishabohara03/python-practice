#Write a program to check whether a given name is present in a list.


# Predefined list of names
name_list = ["Alice", "Bob", "Charlie", "David"]

# Input a name to search
name = input("Enter a name to search: ")

# Check presence
if name in name_list:
    print(f"{name} is in the list.")
else:
    print(f"{name} is not in the list.")
