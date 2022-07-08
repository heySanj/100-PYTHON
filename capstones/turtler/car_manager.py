COLORS = ["red", "orange", "goldenrod", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

# Spawn axis
SPAWN_AREA = (-200, 250)
LANE_SIZE = 25

from car import Car
import random

class CarManager:
    
    def __init__(self):
        self.car_list = []
        self.speed = STARTING_MOVE_DISTANCE
        
    def random_start(self):
        return random.randrange(SPAWN_AREA[0],SPAWN_AREA[1],LANE_SIZE)
    
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Car(random.choice(COLORS), self.random_start())
            self.car_list.append(new_car)
        
    def inc_speed(self):
        self.speed += MOVE_INCREMENT
    
    def move_cars(self):
        for car in self.car_list:
            if car.xcor() <= -350:
                self.car_list.remove(car)
            else:
                car.move(self.speed)

                
            