import smtplib
import datetime as dt
import random

now = dt.datetime.now()

my_email = "dummy_baba@gmail.com"
password = "487823ujsdkljal"
if now.weekday() == 0:
    with open("quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        random_quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="ajay064585@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{random_quote}")
