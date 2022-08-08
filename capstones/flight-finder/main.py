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


# ---------------------------- MAIN PROGRAM ------------------------------- # 



'''
Use the Flight Search and Sheety API to populate your own copy of the Google Sheet
with International Air Transport Association (IATA) codes for each city. Most of the
cities in the sheet include multiple airports, you want the city code (not the airport code see here).
'''
sheet = DataManager()
searcher = FlightSearch()

# Populate the sheets IATA codes
for location in sheet.data:
    if location['iataCode'] == "":
        # print(searcher.get_city_code(location['city']))
        code = searcher.get_city_code(location['city'])
        sheet.put_data(location['id'],"iataCode",code)
        

# data = searcher.get_city_code("tokyo")

# print(json.dumps(data, indent=4, sort_keys=True))