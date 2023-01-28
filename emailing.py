import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv
from news_extractor import ApNews, TechCrunch, Reuters
from newsplease import NewsPlease
from news_summarizer import OpenAIGPT

load_dotenv("./.env")

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_EMAIL_PASSWORD_APP")

recipient_email_address = input("Please enter your email address: ")

now = dt.datetime.now()
weekday = now.weekday()
today = dt.date.today()

# if weekday == 2: # 0 is Monday
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)

#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(from_addr=MY_EMAIL,
#                             # to_addrs=MY_EMAIL,
#                             to_addrs=recipient_email_address,
#                             msg=f"Subject: Monday Motivation\n\n{quote}\n\n"
#                             )

tech = TechCrunch()
tech_top_article = NewsPlease.from_url(tech.get_top_news_url())
gpt_summarizer = OpenAIGPT()
summarized_tech_news = f"Title: {tech_top_article.title}\n{gpt_summarizer.summarize(tech_top_article.maintext)}"


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        # to_addrs=MY_EMAIL,
                        to_addrs=recipient_email_address,
                        msg=f"Subject: TechCrunch Main News {str(today)}\n\n{summarized_tech_news}\n\n"
                        )