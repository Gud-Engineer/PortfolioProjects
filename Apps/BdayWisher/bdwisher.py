"""
Python program to automate birthday wishes and send them using email SMTP

"""
import os
import pandas
import random
import json
import smtplib
from datetime import datetime as dt
from dotenv import load_dotenv


def letter_templates():
    """
    Picks one letter template from letters.json
    :return: <str> letter template
    """
    # TODO : Picking Random Birthday wisher template : JSON has 3 files -> b:3
    template = "letter" + str(random.randint(1, 3))
    # TODO : Gathering the text of the letter from the template picked
    with open("Data/Letters.json") as letters:
        letter = json.load(letters)
        my_letter = letter[template]["body"]
        # print(my_letter)
        # print(type(my_letter))

    return my_letter


def birthday_message():
    """
    Checks birthday.csv against current date to pick out the birthday details
    :return: <list>Letter that will go in message body with all placeholders replaced with details,email of b'day person
    """
    # TODO : Parse birthday.csv and see if there is any birthday today
    today = dt.now()
    today_tuple = (today.month, today.day)
    birthday_data = pandas.read_csv('./Data/birthdays.csv')
    # TODO : Create b'day dict for person1,person1@gmail.com,1995,12,24 : (12,24):Person1,person1@gmail.com,1995,12,24
    birthday_dict = {
        (data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday_data.iterrows()
    }
    # TODO : Check if today matches any in birthday dict
    if today_tuple in birthday_dict:
        birthday_person = birthday_dict[today_tuple]
        # print(birthday_person)
        # print(birthday_person["name"])
        # TODO : Gather a random letter
        contents = letter_templates()
        message = contents.replace("[NAME]", birthday_person["name"])
        message = message.replace("[SENDER]", "Pycharm-GudDeveloper")
        return [message, birthday_person["email"]]


# TODO : Loading environment variables

load_dotenv()
# Gathering My Secrets from environment variables, .gitignore has ignored .env file
my_email = os.getenv("MY_EMAIL")
app_pwd = os.getenv("APP_PASSWORD")  # Application Password for mail.
send_address = birthday_message()[1]

# TODO: Establish connection using Short Message Transfer Protocol
with smtplib.SMTP("smtp.gmail.com") as connection:
    # TODO: Secure connection to mail server -> start Transport layer security; starttls()
    connection.starttls()
    # TODO: Login to mail
    connection.login(user=my_email, password=app_pwd)
    # TODO: Send Email
    # msg="Subject:Subject\n\nMail body
    connection.sendmail(from_addr=my_email,
                        to_addrs=send_address,
                        msg=f"Subject: Happy Birthday !!\n\n{birthday_message()[0]}!!")
