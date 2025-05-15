#2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file Hi-score.txt which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

def game():
    return int(input("Enter your game score: "))

score = game()

try:
    with open("Hi-score.txt", "r") as f:
        hi_score = f.read()
        hi_score = int(hi_score) if hi_score.strip() else 0
except FileNotFoundError:
    hi_score = 0

if score > hi_score:
    with open("Hi-score.txt", "w") as f:
        f.write(str(score))
    print("New high score!")
else:
    print("Try again to beat the high score!")
