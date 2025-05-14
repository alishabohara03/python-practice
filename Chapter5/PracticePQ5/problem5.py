#Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.



fav_languages = {}
for i in range(4):
    name = input(f"Enter friend's name ({i+1}/4): ")
    language = input(f"Enter {name}'s favorite language: ")
    fav_languages[name] = language

print(fav_languages)







#  If the names of 2 friends are same; what will happen to the program in problem 6?

# Answer:
# If two names are the same, the value will be overwritten for that name in the dictionary. Only the last entered value for that name will be saved.

#  If languages of two friends are same; what will happen to the program in problem 6?

# Answer:
# The program will work fine. Dictionary allows duplicate values; only keys (names) need to be unique.