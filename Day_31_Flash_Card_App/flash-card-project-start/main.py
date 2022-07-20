from tkinter import *
import pandas
import random
# ---------------------------- Constants ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT_DESIGN = ("Ariel", 30, "italic")
ANSWER_FONT_DESIGN = ("Ariel", 40, "bold")
# ---------------------------- Random Data ------------------------------- #
to_learn = {}
try:
    data_csv = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_csv = pandas.read_csv("data/french_words.csv")
    to_learn = data_csv.to_dict(orient="records")
except ValueError:
    print("You have already learned 100 words.")
else:
    to_learn = data_csv.to_dict(orient="records")

current_card = {}
removed_word = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(center_background, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(learn_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(learn_word, text=current_card["English"], fill="white")
    canvas.itemconfig(center_background, image=card_back)


def remove_learned_words():
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
center_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="title", font=LANGUAGE_FONT_DESIGN)
learn_word = canvas.create_text(400, 263, text="word", font=ANSWER_FONT_DESIGN)
canvas.grid(column=0, row=0, columnspan=2)
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)
right_button = Button(image=right_image, highlightthickness=0, command=remove_learned_words)
right_button.grid(column=1, row=1)

next_card()
window.mainloop()
