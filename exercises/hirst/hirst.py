def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


clear()

from turtle import Turtle, Screen
import colorgram
import random

# # Get colours
# def get_colours():
#     colours = colorgram.extract("palette.jpg", 36)
#     colour_list = []
#     for colour in colours:
#         r = colour.rgb[0]
#         g = colour.rgb[1]
#         b = colour.rgb[2]
#         colour_list.append((r, g, b))
#     return colour_list


# palette = get_colours()

palette = [
    (26, 109, 164),
    (194, 38, 81),
    (237, 161, 50),
    (234, 215, 86),
    (227, 237, 229),
    (222, 137, 176),
    (143, 109, 57),
    (101, 197, 219),
    (206, 166, 29),
    (21, 58, 132),
    (212, 75, 91),
    (238, 89, 49),
    (141, 208, 227),
    (119, 192, 141),
    (6, 160, 87),
    (4, 186, 179),
    (106, 108, 198),
    (136, 29, 72),
    (98, 51, 37),
    (25, 153, 211),
    (228, 168, 188),
    (153, 213, 195),
    (173, 186, 221),
    (234, 174, 162),
    (30, 91, 95),
    (87, 47, 34),
    (34, 46, 84),
    (239, 203, 10),
    (33, 85, 84),
    (95, 27, 52),
]



timmy = Turtle()
screen = Screen()
screen.colormode(255)


# Change shape and settings
screen_w = 800
screen_h = 800
timmy.speed(30)

screen.setup(screen_w, screen_h)

# Generate dots
def dot_grid(columns, rows, size):
    timmy.up()
    for r in range(rows):
        spacing = (r+1) * (screen_h / (rows+1))
        timmy.goto(-screen_w / 2, (-screen_h / 2) + spacing)
        for c in range(columns):
            timmy.forward(screen_w / (columns+1))            
            timmy.dot(size, random.choice(palette))
            


dot_grid(10, 10, 35)

# Exit on click at the end of the code
screen.exitonclick()
