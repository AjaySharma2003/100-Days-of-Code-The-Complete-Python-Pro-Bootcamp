import turtle
import pandas

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 State Correct", prompt="What's another state name?").title()
    all_states = data["state"].to_list()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data["state"] == answer_state]
        t.goto(int(state.x), int(state.y))
        t.write(answer_state)
not_guessed_states = [i for i in all_states if i not in guessed_state]
df = pandas.DataFrame(not_guessed_states, columns=["Not_Guessed_State"] )
df.to_csv("not_guessed_states.csv")




# 1)Convert the guess to title case
# 2)Check if the guess is among the 50 states
# 3)Write correct guesses onto the map
# 4)Use a loop to allow the to keep guessing
# 5)Record the correct guesses in a list
# 6)Keep track of the Score
