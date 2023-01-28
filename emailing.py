import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv

load_dotenv("./.env")

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_EMAIL_PASSWORD_APP")

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 2: # 0 is Monday
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject: Monday Motivation\n\n{quote}\n\n"
                            )