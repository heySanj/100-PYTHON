import os
clear = lambda: os.system('clear')
clear()

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
action = input("\nYou're at a crossroad, where do you want to go? Type 'left' or 'right'.\n").lower()

if action == "left":
    action = input("\nYou arrive at a river with rapidly flowing water. Do you try and 'swim' or 'wait'?\n").lower()
    if action == "wait":
        action = input('''\nYou wait for the waters to die down, revealing a crossing.
After crossing, you arrive at a cottage with 'red', 'yellow' and 'blue' doors.
Which door do you open?\n''').lower()
        if action == "red":
            print("\nYou enter a room filled with flames! Game Over...")
        elif action == "yellow":
            print("\nYou enter a room illuminated by treasure! You Win!!!")
        elif action == "blue":
            print("\nYou enter a room full of beasts and are devoured! Game Over...")
        else:
            print("\nGame Over...")
    else:
        print("\nYou try to swim but get attacked by a school of trout! Game Over...")
else:
    print("\nYou fall into a hole! Game Over...")