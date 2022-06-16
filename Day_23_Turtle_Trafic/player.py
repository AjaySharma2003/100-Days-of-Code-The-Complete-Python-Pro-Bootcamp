from turtle import Turtle
from car_manager import CarManager

car_manager = CarManager()
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def move_up(self):
        if self.xcor() >= 280:
            self.goto(STARTING_POSITION)
        else:
            self.forward(MOVE_DISTANCE)

    def check_game_over(self):
        for car in car_manager.cars:
            if self.distance(car) < 15:
                return True
