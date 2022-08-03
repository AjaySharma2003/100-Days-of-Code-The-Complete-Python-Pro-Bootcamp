import smtplib
import random
import datetime as dt
import pandas
# ---------------------------- mail ------------------------------- #


def create_mail():
    random_letter = random.choice(letters)
    letter_to_sent = random_letter.replace("[NAME]", name)
    my_email = "dummybaba4585@gmail.com"
    password = "wqfripujkxyvefen"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_mail, msg=f"Subject:Happy Birthday!!\n\n{letter_to_sent}")


today_date_info = dt.datetime.now()
birthdays = pandas.read_csv("birthdays.csv")
letters = []
with open("letter_templates/letter_1.txt") as letter:
    letter_1 = letter.read()
    letters.append(letter_1)
with open("letter_templates/letter_2.txt") as letter:
    letter_2 = letter.read()
    letters.append(letter_2)
with open("letter_templates/letter_3.txt") as letter:
    letter_3 = letter.read()
    letters.append(letter_3)
today_month = str(today_date_info.date().month)
today_day = str(today_date_info.date().day)
today_date = today_month + today_day
month = 0
day = 0
name = ""
birthday_date = month + day
for i in range(len(birthdays)):
    month = str(birthdays["month"][i])
    day = str(birthdays["day"][i])
    name = birthdays["name"][i]
    to_mail = birthdays["email"][i]
    birthday_date = month + day
    if today_date == birthday_date:
        create_mail()
