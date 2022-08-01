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

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ.get("OWM_API_KEY")
MY_LAT = -27.469770 # Your latitude
MY_LONG = 153.025131 # Your longitude


import requests
import json

# ---------------------------- TWILIO ------------------------------- # 
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH")

SEND_NUMBER = os.environ.get("TWILIO_NUMBER")
TO_NUMBER = os.environ.get("PH_NUM")

client = Client(account_sid, auth_token)

def send_sms():
    
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an umbrella! ☔",
                     from_= SEND_NUMBER,
                     to= TO_NUMBER
                 )
    print(message.status)

# ---------------------------- WEATHER CHECK ------------------------------- # 

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily,alerts",
    "appid": API_KEY
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()
hourly_data = weather_data['hourly']

# Print out he JSON Data
# print(json.dumps(weather_data, indent=4, sort_keys=True))
# print(weather_data)

# For the first 12 hours in the retreived hourly data
for hour in hourly_data[:12]:
    
    status_code = hour['weather'][0]['id']
    
    # If there is any rain at all, send a warning
    if status_code < 700:
        send_sms()
        # print("Rain!")
        break
    