from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)
font_mode = ("Arial", 14)
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)
miles_input.insert(END, string="0")
miles_input.get()

miles_label = Label(text="Miles", font=font_mode)
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=font_mode)
equal_label.grid(column=0, row=1)

km_output = Label(text=0, font=font_mode)
km_output.grid(column=1, row=1)

km_label = Label(text="Km", font=font_mode)
km_label.grid(column=2, row=1)


def converter():
    miles = int(miles_input.get())
    Km = round(miles * 1.6)
    km_output.config(text=Km)


button = Button(text="Calculate", font=font_mode, command=converter)
button.grid(column=1, row=2)

window.mainloop()
