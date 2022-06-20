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

timmy = Turtle()
screen = Screen()

# Change shape and settings
timmy.shape('turtle')
timmy.color('coral')

# Exit on click at the end of the code
screen.exitonclick()