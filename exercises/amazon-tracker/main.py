def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

import os
import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp
from smtp.mail_message import Email

# -------------- SOUP -------------------

URL = "https://amzn.asia/d/5WugASH"
HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language":"en-AU,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding":"gzip, deflate",
    "Connection":"keep-alive"
}

TARGET_PRICE = 60.0

# Get HTML
response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.text, 'html.parser')

# Get Price
cost_string = soup.select("span.a-offscreen")[0].getText()
cost = float(cost_string[1:])

# If price is below the target -- send an email alert!
if cost <= TARGET_PRICE:
    print(f"Product is cheap ({cost_string}) -- sending email...")
    
    message = Email(
        username=os.environ.get("EMAIL_USER"),
        password=os.environ.get("EMAIL_PASS"),
        sender="Python Price Tracker",
        recipient=os.environ.get("RECIPIENT"),
        subject="Amazon Price Alert!",
        message=f"A product on your watchlist is on sale for {cost_string}! \n{URL} \nSent using the Python Price Tracker!"
    )
    
    message.send()
    
else:
    print(f"Product is expensive - {cost_string}! 😥")

print("\n")

