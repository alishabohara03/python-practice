
#Write a program to read the text from a given file poems.txt and find out whether it contains the word 'twinkle'.

# Open the file in read mode
with open("poems.txt", "r") as file:
    content = file.read()

# Check if the word 'twinkle' is in the content
if 'twinkle' in content.lower():
    print("The word 'twinkle' is present in the file.")
else:
    print("The word 'twinkle' is NOT present in the file.")
