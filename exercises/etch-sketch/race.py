def clear():
    from os import system, name  
    # for windows
    if name == 'nt':
        _ = system('cls')  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
clear()

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)



# Setup
colours = {'red3': 'red', 
           'royalblue3': 'blue',
           'gold': 'yellow',
           'medium orchid': 'purple',
           'medium sea green': 'green',
           'gray22': 'black',
           }

ycord = -120

turtles = []

for t in colours:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(t)
    new_turtle.penup()
    new_turtle.goto(x=-200,y=ycord)
    ycord += 50
    turtles.append(new_turtle)

# Race
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")

if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)
        # Check win
        if turtle.xcor() >= 230:
            race_on = False
            winning_colour = colours[turtle.pencolor()]
            break


if winning_colour == user_bet:
    print(f"Hooray you Won! {winning_colour.title()} has won the race! 🏆")
else:
    print(f"Sorry {user_bet.title()} lost...{winning_colour.title()} won the race 😥")

# Exit on click at the end of the code
screen.exitonclick()