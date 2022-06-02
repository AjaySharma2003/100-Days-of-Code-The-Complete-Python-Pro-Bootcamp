from turtle import Turtle, Screen
import turtle
import random
turtle.colormode(255)
tim = Turtle()
color_list = [(193, 152, 91), (131, 80, 53), (232, 225, 227),  (135, 177, 202),
              (59, 95, 146), (120, 68, 75), (218, 203, 115), (191, 132, 160), (129, 192, 160), (200, 86, 63),
              (185, 92, 118), (219, 226, 233), (84, 122, 77), (73, 57, 47), (97, 96, 161), (160, 200, 209),
              (108, 147, 53), (106, 50, 56), (171, 192, 214), (214, 178, 188), (221, 179, 170), (82, 57, 51),
              (172, 203, 186), (74, 64, 51), (116, 137, 112), (41, 63, 98), (75, 45, 48), (92, 136, 159)]
tim.penup()
tim.setheading(205)
tim.forward(400)
tim.setheading(0)

for i in range(10):
    for _ in range(10):
        col = random.choice(color_list)
        tim.dot(24, col)
        tim.penup()
        if _ != 9:
            tim.forward(50)
    if i % 2 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
    else:
        tim.right(90)
        tim.forward(50)
        tim.right(90)
tim.hideturtle()
screen = Screen()
screen.exitonclick()
