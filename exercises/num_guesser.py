import random
import os
clear = lambda: os.system('clear')
clear()

logo = """
   _____                       _   _            _   _                 _               
  / ____|                     | | | |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                      
                                                                                      """

print(logo)                                                                                      
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
goal = random.randint(1,100)

difficulty = input("\nChoose a difficulty. Type 'easy' or 'hard': ")


if difficulty == "easy":
    chances = 10
else:
    chances = 5
    
def compare(guess):
    global goal
    if guess == goal:
        return "win"
    elif guess > goal:
        return "Too High."
    elif guess < goal:
        return "Too Low"
    
while chances > 0:
    print(f"\nYou have {chances} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
    if compare(guess) == "win":
        print(f"\nYou got it! The answer was {goal}.\n\n")
        quit()
    else:
        print(compare(guess))        
        chances -= 1
        if chances > 0:
            print("Guess again.")
        
print(f"\nSorry, you're out of guesses. The answer was {goal}.\n\n")