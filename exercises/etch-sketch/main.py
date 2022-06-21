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

tim = Turtle()
screen = Screen()


# Functions
def move_forward():
    tim.forward(10)
    
def move_back():
    tim.backward(10)
    
def right():
    tim.right(30)
    
def left():
    tim.left(30)
    

# Controls
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=tim.clear)

# Exit on click at the end of the code
screen.exitonclick()