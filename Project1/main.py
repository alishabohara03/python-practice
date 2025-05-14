import random

# ---------------------------
# SUPERCLASS
# ---------------------------
class Game:
    def __init__(self, player_name="Player"):
        self._player_name = player_name
        self._score = 0
        self.choices = ["snake", "water", "gun"]
        self.history = []

    @property
    def player_name(self):
        return self._player_name

    @property
    def score(self):
        return self._score

    def update_score(self, result):
        if result == "win":
            self._score += 1

    def show_history(self):
        print("\nGame History:")
        for round_result in self.history:
            print(round_result)

# ---------------------------
# MULTILEVEL INHERITANCE
# ---------------------------
class Rules(Game):
    def determine_winner(self, user, computer):
        if user == computer:
            return "draw"
        win_map = {
            "snake": "water",
            "water": "gun",
            "gun": "snake"
        }
        return "win" if win_map[user] == computer else "lose"

# ---------------------------
# MULTIPLE INHERITANCE
# ---------------------------
class Display:
    def escape_example(self):
        print("Escape Example:\nSnake\tWater\tGun\nLet's Play!\n")

# ---------------------------
# MAIN GAME CLASS
# ---------------------------
class SnakeWaterGun(Rules, Display):
    def __init__(self, player_name="Player"):
        super().__init__(player_name)

    def play_round(self, user_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)
        self.update_score(result if result == "win" else "")
        outcome = f"You chose {user_choice}, computer chose {computer_choice}. Result: {result.title()}"
        self.history.append(outcome)
        print(outcome)

    # Operator overloading
    def __gt__(self, other):
        return self.score > other.score

# ---------------------------
# FUNCTION, DEFAULT ARG, RECURSION
# ---------------------------
def quick_quiz(score=0):
    questions = {
        "What does '==' do?": "comparison",
        "What is the keyword to define a function?": "def",
        "Which data type is immutable: list or tuple?": "tuple"
    }
    def ask(q_list, index=0, score=0):
        if index == len(q_list):
            return score
        q = list(q_list.keys())[index]
        ans = input(q + " ").strip().lower()
        if ans == q_list[q]:
            score += 1
        return ask(q_list, index + 1, score)

    final_score = ask(questions)
    print(f"\nYour quiz score is {final_score}/{len(questions)}\n")

# ---------------------------
# MAIN LOOP
# ---------------------------
def main():
    name = input("Enter your name: ")
    game1 = SnakeWaterGun(name)
    game2 = SnakeWaterGun("Computer")

    game1.escape_example()

    while True:
        print("\nChoices: snake, water, gun")
        choice = input("Your move (or type 'quit', 'quiz', 'history'): ").lower()

        if choice == 'quit':
            break
        elif choice == 'quiz':
            quick_quiz()
            continue
        elif choice == 'history':
            game1.show_history()
            continue
        elif choice not in game1.choices:
            print("Invalid choice.")
            continue

        game1.play_round(choice)

    print(f"\nFinal Score: {game1.player_name} = {game1.score}")
    print("Thanks for playing!")

    # Operator Overloading Test
    print("\nWho played better?")
    if game1 > game2:
        print(f"{game1.player_name} wins overall!")
    else:
        print(f"{game2.player_name} wins overall!")

if __name__ == "__main__":
    main()

