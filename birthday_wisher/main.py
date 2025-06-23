import smtplib
import datetime as dt
import random
import os

MY_EMAIL = os.getenv("EMAIL_KEY") # set your email as environment variable (EMAIL_KEY)
MY_PASSWORD = os.getenv("PASSWORD_KEY") # set your password(app password) as environment variable (PASSWORD_KEY)

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0: # here you can add your birthdate
    with open("quotes.txt") as quotesfile:
        all_quotes = quotesfile.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"

        )
