from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        website = website_input.get()
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No data file Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email : {email} \n Password : {password}")
        else:
            messagebox.showwarning(title="Error", message=f"No details for {website} exists.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter = [choice(letters) for _ in range(randint(8, 10))]
    symbol = [choice(symbols) for _ in range(randint(2, 4))]
    number = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letter + symbol + number
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_given = website_input.get()
    email_given = email_input.get()
    password_given = password_input.get()
    new_data = {
        website_given: {
            "email": email_given,
            "password": password_given,
        }
    }
    if len(website_given) == 0 or len(password_given) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2)
email_input.insert(END, "ajay@gmail.com")

password_input = Entry(width=35)
password_input.grid(column=1,  row=3)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4)
window.mainloop()
