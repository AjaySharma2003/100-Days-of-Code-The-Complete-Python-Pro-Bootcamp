from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=1000, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "lime", "light cyan", "dark gray" ]
all_turtles = []
y = -200
for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-470, y=y)
    all_turtles.append(new_turtle)
    y += 50

if user_bet:
    is_race_on = True


def start():

    is_race_on = True
    while is_race_on:

        for turtle in all_turtles:
            if turtle.xcor() > 460:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've Won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)


screen.listen()
screen.onkey(key="space", fun=start)
screen.exitonclick()
