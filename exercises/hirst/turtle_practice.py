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
import random

timmy = Turtle()
screen = Screen()
screen.colormode(255)

# Functions
def random_color():
    '''Make Timmy a random color'''
    timmy.pencolor( random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255))

def timmy_square(size):
    '''Draw a square of size'''
    timmy.begin_fill()
    for _ in range(4):
        timmy.forward(size)
        timmy.right(90)
    timmy.end_fill()

def dash_line(dash, length):
    '''Draw a line of length, with adjustable dash size'''
    for _ in range(length):
        timmy.forward(dash)
        timmy.pu()
        timmy.forward(dash)
        timmy.pd()      

def all_shapes(sides, size):
    '''Draw all polygons up to the number of sides'''
    for i in range(3, sides):
        # Change colour
        random_color()
        for _ in range(i):
            timmy.forward(size)
            timmy.right(360 / i)
        i += 1

def random_walk(size, steps):
    '''Randomly move in a direction for x amount of steps'''
    direction = [0, 90, 180, 270]
    for _ in range(steps):
        # Choose random direction
        timmy.setheading(random.choice(direction))
        # Colour and move
        random_color()
        timmy.forward(size)

# Change shape and settings
timmy.pensize(15)
timmy.speed(8)
        
# Do something
random_walk(30, 150)

# Exit on click at the end of the code
screen.exitonclick()