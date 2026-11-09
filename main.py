#name: RIDLEY CADET
#QCC ID: 24812130

import random 

class Die:
    def __init__(self, sides=6):
       self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)
    
class DiceGame:
        def __init__(self):
            self.die1 = Die()
            self.die2 = Die() 

        def evaluate_roll(self, total):
            if total in [7,11]:
                return "Win"
            elif total in [2,3,12]:
                return "Lose"
            else:
                return "Roll Again"

        def play_round(self):
            roll1 = self.die1.roll()
            roll2 = self.die2.roll()
            total = roll1 + roll2
            result = self.evaluate_roll(total)

            return roll1, roll2, total, result

def main():
        game = DiceGame()

        while True:
            print("\n=== Dice Game ===")
            print("1. play a round")
            print("2. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                die1, die2, total, result = game.play_round()

                print(f"First die: {die1}")
                print(f"second die: {die2}")
                print(f"Total: {total}")
                print(f"Result: {result}")

            elif choice == "2":
                print("Thanks for playing!")
                break
            else:
                print("invalid choice. Please try again.")


if __name__ == "__main__":
    main()