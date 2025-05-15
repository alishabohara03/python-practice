#4. A file contains the word "Donkey" multiple times. You need to write a program which replaces this word with ###### by updating the same file.

with open("donkey.txt", "r") as f:
    content = f.read()

content = content.replace("Donkey", "######")

with open("donkey.txt", "w") as f:
    f.write(content)

