import random
from turtle import Turtle, Screen
screen = Screen()
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.cars = []
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 5

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            screen.tracer(0)
            new_car = Turtle()
            color = random.choice(COLORS)
            new_car.shape("square")
            new_car.color(color)
            new_car.penup()
            new_car.turtlesize(stretch_wid=1.1, stretch_len=3)
            new_car.setheading(180)
            new_y = random.randrange(-300, 300)
            new_car.goto(320, new_y)
            screen.update()
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.forward(self.STARTING_MOVE_DISTANCE)

    def update_car_speed(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT
