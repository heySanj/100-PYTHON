def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

STOCK = "UBER"
COMPANY_NAME = "Uber Technologies"

import os
import requests
import json
from datetime import datetime, timedelta

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
 
# ---------------------------- TWILIO ------------------------------- # 
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH")

SEND_NUMBER = os.environ.get("TWILIO_NUMBER")
TO_NUMBER = os.environ.get("PH_NUM")

client = Client(account_sid, auth_token)

def send_sms(message):
    
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    
    message = client.messages \
                .create(
                     body=message,
                     from_= SEND_NUMBER,
                     to= TO_NUMBER
                 )
    print(message.status)
    
    
# ---------------------------- STOCK API ------------------------------- # 

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def check_stock(symbol):
    AA_ENDPOINT = "https://www.alphavantage.co/query"
    AA_API_KEY = os.environ.get("AA_API_KEY")


    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "datatype": "json",
        "apikey": AA_API_KEY
    }

    # Connect to Alpha Advantage endpoint using above parameters
    response = requests.get(url=AA_ENDPOINT, params=parameters)
    response.raise_for_status()

    # Get the data, ignoring the metadata
    stock_data = response.json()['Time Series (Daily)']

    # Print out the JSON Data
    # print(json.dumps(last_close, indent=4, sort_keys=True))

    # Get closing value from the last two days
    yesterday_value = float(list(stock_data.values())[0]['4. close'])
    original_value = float(list(stock_data.values())[1]['4. close'])

    # Calculate percentage increase
    change = ((yesterday_value - original_value) / original_value) * 100
    change = round(change, 2)
    
    # print(f"{yesterday_value}\n{original_value}\nDifference of {change:.2f}%")
    
    return change
    

# ---------------------------- NEWS API ------------------------------- # 

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def get_news(change):
    
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

    # Get yesterdays date and format to YYYY-MM-DD
    yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')  

    parameters = {
        "q": COMPANY_NAME, # question must be URL encoded
        "searchIn": "title",
        "from": yesterday, # From date onwards
        "language": "en",
        "apikey": NEWS_API_KEY
    }

    # Connect to NEWS endpoint using above parameters
    response = requests.get(url=NEWS_ENDPOINT, params=parameters)
    response.raise_for_status()

    # Get a list of the first 3 articles
    news_data = response.json()["articles"][:3]
    
    # Print out the JSON Data
    # print(json.dumps(news_data, indent=4, sort_keys=True))
    
    emoji = "🔻"
    if change >= 0: emoji = "💹"
    
    stock_header = f"{STOCK} {emoji} {abs(change)}%"
    
    # Format a message for each article and send it
    for article in news_data:
        headline = article['title']
        brief = article['description']
        
        message = (f"\n\n{stock_header}\n\nHeadline: {headline}\n\nBrief: {brief}\n\n")
        
        # Send the message
        # print(message)
        send_sms(message)
    

# ---------------------------- MAIN PROGRAM FUNCTION ------------------------------- # 

# Check the stock
change = check_stock(STOCK)

# If the value is greater than 5 -> then get news
if abs(change) >= 5:
    get_news(change)    
else:
    print("Not much change")