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

# ---------------------------- SENDING EMAILS ------------------------------- #

from mail_message import Email

def send_email(subject, message):
    
    new_email = Email(
        username="test@testmail.com",
        password="abcd1234",
        sender="Python Motivational Mailer",
        recipient="test@testmail.com",
        subject=subject,
        message=message
    )
    
    # Send it
    new_email.send()

# ---------------------------- GET QUOTES ------------------------------- #

# Get a list of names
with open("quotes.txt") as file:
    quotes = file.readlines()

# ---------------------------- PROGRAM ------------------------------- #

now = dt.datetime.now() # Current date and time as a datetime Class

# Is it a monday?
if now.weekday() == 3:
    # Send a motivational quote
    send_email("Wise words for your day!", choice(quotes))

