#Write a program to greet all the person names stored in a list l and which starts with 'S'.

names = ["Harry", "Soham", "Sachin", "Rahul"]
for name in names:
    if name.startswith('S'):
        print(f"Hello {name}")
