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

import json
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

HOME_AIRPORT = "BNE"

# ---------------------------- MAIN PROGRAM ------------------------------- # 

'''
Use the Flight Search and Sheety API to populate your own copy of the Google Sheet
with International Air Transport Association (IATA) codes for each city. Most of the
cities in the sheet include multiple airports, you want the city code (not the airport code see here).
'''
sheet = DataManager() # Establish a connection to the Google sheets
searcher = FlightSearch() # Establish a connection to the flight search engine

tomorrow = dt.today() + relativedelta(days=+1)
six_months = tomorrow + relativedelta(months=+6)

# Loop through the Google sheet data
for location in sheet.data:
    
    # If there is no IATA code present -> Generate it through the search engine
    if location['iataCode'] == "":
        code = searcher.get_city_code(location['city'])
        sheet.put_data(location['id'],"iataCode",code)
        
    # Check for the cheapest flights from Tomorrow to 5 months later
    flights = searcher.search(HOME_AIRPORT, location['iataCode'], tomorrow.strftime("%d/%m/%Y"), six_months.strftime("%d/%m/%Y"), location['lowestPrice'])['data']
    
    # If cheaper flights are found
    if len(flights) > 0:
        flight = FlightData(flights[0]) # get the first flight
        print(flight.get_details())
    
    
    
    # flights_list = []

    # for flight in flights:
    #     new_flight = FlightData(flight)
    #     flights_list.append(new_flight)
    #     print(new_flight.get_details())
    
    
    # If the price is lower than the one stored on the sheet -> send an alert!
        








# print(json.dumps(flights, indent=4, sort_keys=True))