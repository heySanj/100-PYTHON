import os
clear = lambda: os.system('clear')
clear()


import random
from ascii import logo, stages
from words import word_list



# Generate a random word
word = random.choice(word_list)
guess_arr = list("_" * len(word))

# Check the letter and update the guess blanks
def check_letter(letter):
    letter_found = False
    for i in range(len(word)):
        if word[i] == letter:
            guess_arr[i] = word[i]
            letter_found = True
    return letter_found
    
# Draw Hangman
def draw_hangman():
    clear()
    print(logo)
    print("\n================================================")
    print(f"Pssst, the solution is {word}.")
    print(stages[chances])
    print(f"Chances left: {chances}\n")
    print(' '.join(guess_arr))
    
# Winning scenario
def win():
    draw_hangman()
    print("================================================\n")
    print("YOU WIN!\n")
    
# Losing scenario
def lose():
    draw_hangman()
    print("================================================\n")
    print(f"YOU LOSE! The word was: {word}.\n")

chances = len(stages) - 1

while True:
    
    draw_hangman()
    
    guess = input("\nGuess a letter.\n").lower()
    
    if not check_letter(guess):
        chances -= 1     
    
    if chances < 0:
        lose()
        break
    elif "_" not in guess_arr:
        win()
        break

