from turtle import Turtle
import random

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """Create a Snake object"""  
    
    def __init__(self):
        self.snake_body = []        
        self.create_snake()
        self.head = self.snake_body[0]
        


    # Functions
    def create_snake(self):
        '''Create the initial snake'''         
        for position in STARTING_POSITIONS:
            self.add_part(position, self.random_colour())
    
    def add_part(self, pos, colour):
        '''Add a part to the snake'''
        new_turtle = Turtle('square')
        new_turtle.color(colour)
        new_turtle.penup()
        
        # Move the body part to position
        new_turtle.goto(pos)
        self.snake_body.append(new_turtle)
                 
    def move(self):
        '''Move the snake in a chained manner'''
        for part_num in range(len(self.snake_body) - 1, -1, -1):
            if part_num == 0:
                # Move the head forward
                self.head.forward(MOVE_DISTANCE)
            else:
                # Move to the position of the next part
                part = self.snake_body[part_num]
                part.goto(self.snake_body[part_num - 1].pos())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
            
    def random_colour(self):
        # Colour
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))