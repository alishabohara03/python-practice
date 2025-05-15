#5. Repeat program 4 for a list of such words to be censored.

words_to_censor = ["donkey", "idiot", "stupid"]

with open("comments.txt", "r") as f:
    content = f.read()

for word in words_to_censor:
    content = content.replace(word, "######")

with open("comments.txt", "w") as f:
    f.write(content)
