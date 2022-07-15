def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

FONT = ('Arial', 8, 'bold')

from types import NoneType
import pandas as pd
from turtle import Turtle, Screen

# Set up the writer
writer = Turtle()
writer.hideturtle()        
writer.pencolor('black')
writer.penup()  

# Screen setup
screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic("./images/blank_states_img.gif")
screen.title('U.S. States Game')
screen.colormode(255)


def write_label(text, pos):
    writer.goto(pos)
    writer.write(text, align='center', font=FONT)
    
# Get data from CSV
data = pd.read_csv("./data/50_states.csv")

states_list = data.state.to_list()

score = 0
    
while score < 50:
    pass
    # Ask the player for a guess
    guess = screen.textinput(f"{score}/50 States Named", "Guess a state name")
    

    if type(guess) == NoneType:
        break        
    elif guess.title() == 'Exit' or score >= 50:
        break
    else:
        guess = guess.title()
           
        # Check Guess
        if guess in states_list:
            states_list.remove(guess)
            score += 1
            # Get state data
            state_data = data[data.state == guess]
            write_label(state_data.state.item(), (int(state_data.x),int(state_data.y)))
    
# Create csv of states to learn
states_to_learn = pd.Series(states_list)
states_to_learn.to_csv("./data/states_to_learn.csv")   
    
# Exit on click at the end of the code
screen.exitonclick()