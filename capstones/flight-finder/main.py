#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

from pprint import pprint as pp
import json
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

HOME_AIRPORT = "BNE"

# ---------------------------- MAIN PROGRAM ------------------------------- # 

sheet = DataManager() # Establish a connection to the Google sheets
searcher = FlightSearch() # Establish a connection to the flight search engine
message_service = NotificationManager()

tomorrow = dt.today() + relativedelta(days=+1)
six_months = tomorrow + relativedelta(months=+6)

# Loop through the Google sheet data
for location in sheet.price_data:
    
    # If there is no IATA code present -> Generate it through the search engine
    if location['iataCode'] == "":
        code = searcher.get_city_code(location['city'])
        sheet.put_data('prices', location['id'],"iataCode",code)
        
    # Check for the cheapest flights from Tomorrow to 5 months later
    flights = searcher.search(HOME_AIRPORT, location['iataCode'], tomorrow.strftime("%d/%m/%Y"), six_months.strftime("%d/%m/%Y"), location['lowestPrice'])['data']
    
    # If cheaper flights are found
    try:
        flight = FlightData(flights[0]) # get the first flight
        message = flight.get_details()
        
        # If the price is lower than the one stored on the sheet -> update price and send an alert!
        if flight.price < location['lowestPrice'] or location['lowestPrice'] == 0:
            print("UPDATING PRICE")
            # Update price
            sheet.put_data( 'prices', location['id'], "lowestPrice", flight.price)
            
            # Send a text message
            # message_service.send_sms(message=message)
            print(message)
            
            # Send email to all users
            for user in sheet.user_data:
                user_email = user['email']
                user_name = user['firstName']
                subject = f"Flight Deal Alert! Cheap flights to {location['city']}"
                email_message = f"Dear {user_name},\n\n{message}"
                message_service.send_email(user_email, subject, email_message)
                    
    except IndexError:
        print(f"No flights found for {location['iataCode']}.")        
        


