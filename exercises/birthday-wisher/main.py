def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

import datetime as dt
from random import choice
import pandas as pd
from smtp.mail_message import Email
from os import listdir
TEMPLATES_DIRECTORY = "./letter_templates/"

# ---------------------------- SENDING EMAILS ------------------------------- #

def send_email(subject, message):    
    new_email = Email(
        username="test@testmail.com",
        password="abcd1234",
        sender="Sanjeev",
        recipient="test@testmail.com",
        subject=subject,
        message=message
    )    
    # Send it
    new_email.send()
    
    
# ---------------------------- CREATING LETTERS ------------------------------- #

def create_letter(to, age, sender):
    # Get a random letter template and replace with details
    with open(TEMPLATES_DIRECTORY + choice(listdir(TEMPLATES_DIRECTORY))) as file:
        message = file.read()
        message = message.replace("[NAME]", to)
        message = message.replace("[AGE]", age)
        message = message.replace("[FROM]", sender)
    
    return message
        
# ---------------------------- GET THE LIST OF BIRTHDAYS AND CHECK ------------------------------- #

# 1. Update the birthdays.csv

data = pd.read_csv("birthdays.csv")    
birthdays = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now() # Current date and time as a datetime Class

for bday in birthdays:
    # If it is their birthday
    if bday['month'] == now.month and bday['day'] == now.day:
        # create the birthday message
        bday_message = create_letter(bday['name'], str(now.year - bday['year']), "Sanj")
    
        # send the email
        send_email(f"Happy Birthday {bday['name']}!", bday_message)





