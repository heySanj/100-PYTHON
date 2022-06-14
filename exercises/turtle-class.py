# define our clear function
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

# Create a new Turtle object and save as timmy
timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")

# Screen setup
my_screen = Screen()


# Move
timmy.forward(100)



# Exit on click
my_screen.exitonclick()