#Write a python function to remove a given word from a list: and strip it at the same time.

def remove_and_strip(words, word_to_remove):
    return [word.strip() for word in words if word.strip() != word_to_remove]

words = [" apple ", " banana", "apple", " mango "]
print(remove_and_strip(words, "apple"))
