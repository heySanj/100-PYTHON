def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


import requests
from datetime import datetime
from mail_message import Email
import time

MY_LAT = -27.469770 # Your latitude
MY_LONG = 153.025131 # Your longitude

# ---------------------------- ISS LOCATOR ------------------------------- # 

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_close():
    if (MY_LAT-5 <= iss_latitude <= MY_LAT+5) and (MY_LONG-5 <= iss_longitude <= MY_LONG+5):
        return True
    else:
        return False
    
# ---------------------------- SUNSET AND SUNRISE ------------------------------- # 

# Time now
time_now = datetime.now()

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "date": time_now.date(),
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
clear() # Clear any warnings
response.raise_for_status() # Raise exceptions
data = response.json()

# Format the data into a usable format
sunrise = int(data["results"]["sunset"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunrise"].split("T")[1].split(":")[0])


# Is it dark
def is_dark():
    if sunrise <= time_now.hour <= sunset:
        return False
    else:
        return True
    
    
# ---------------------------- SENDING EMAILS ------------------------------- #

def send_email(subject, message):    
    new_email = Email(
        username="test@testmail.com",
        password="abcd1234",
        sender="ISS Locator",
        recipient="test@testmail.com",
        subject=subject,
        message=message
    )    
    # Send it
    new_email.send()

# ---------------------------- PROGRAM ------------------------------- # 
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if is_close and is_dark:
        subject = "The ISS is in your area!",
        message = "Look up! You just might spot the ISS!"
        # send the email
        # send_email(subject, message)


