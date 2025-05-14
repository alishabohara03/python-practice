#A spam comment is defined as containing any of the following:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”
# Write a program to detect spam.


# Input comment from user
comment = input("Enter your comment: ").lower()

# Define spam keywords
spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

# Check if comment contains spam
is_spam = False
for keyword in spam_keywords:
    if keyword in comment:
        is_spam = True
        break

if is_spam:
    print("This is a spam comment.")
else:
    print("This is not a spam comment.")
