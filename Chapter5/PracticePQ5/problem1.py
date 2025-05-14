# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

dictionary = {
    "paani": "water",
    "roti": "bread",
    "kitab": "book",
    "ghar": "home"
}

word = input("Enter a Hindi word to translate: ")
print("English translation:", dictionary.get(word, "Word not found"))
