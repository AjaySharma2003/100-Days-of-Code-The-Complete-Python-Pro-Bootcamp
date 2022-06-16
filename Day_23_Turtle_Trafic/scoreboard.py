from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-250, 250)
        self.hideturtle()
        self.level_display()

    def level_display(self):
        self.write(f"Level : {self.level}", font=FONT)

    def update_score(self):
        self.level += 1
        self.level_display()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", font=FONT)
