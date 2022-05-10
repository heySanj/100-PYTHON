import os
clear = lambda: os.system('clear')
clear()

import random

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# Player chooses
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

# Computer Chooses
opp = random.randint(0, 2)
print("Computer chose:\n")

if opp == 0:
    print(rock)
elif opp == 1:
    print(paper)
else:
    print(scissors)
    
# Determine Winner
if choice == opp:
    print("It's a draw")
elif choice == 0:
    if opp == 2:
        print("You Win!")
    else:
        print("You Lose!")
elif choice == 1:
    if opp == 0:
        print("You Win!")
    else:
        print("You Lose!")
elif choice == 2:
    if opp == 1:
        print("You Win!")
    else:
        print("You Lose!")