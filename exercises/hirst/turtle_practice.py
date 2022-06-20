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
import heroes

timmy = Turtle()
screen = Screen()

# Functions
def timmy_square(size):
    '''Draw a square of size'''
    timmy.begin_fill()
    for _ in range(4):
        timmy.forward(size)
        timmy.right(90)
    timmy.end_fill()
        

# Change shape and settings
timmy.shape('turtle')
timmy.color('coral')
        
# Do something
timmy_square(30)
print(heroes.gen())

# Exit on click at the end of the code
screen.exitonclick()