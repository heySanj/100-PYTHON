import os
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
            
        self.TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
        self.TEQUILA_KEY = os.environ.get("TEQUILA_KEY")
        self.HEADERS = {
            "apikey": self.TEQUILA_KEY
        }
        self.currency = "AUD"
        self.min_nights = 5
        self.max_nights = 30
    
    # Return the city code of input city
    def get_city_code(self, city: str) -> str:
        location_ep = f"{self.TEQUILA_ENDPOINT}/locations/query"
        
        parameters = {
            "term": city
        }
        
        response = requests.get(url=location_ep, headers=self.HEADERS, params=parameters)
        code = response.json()['locations'][0]['code']
                
        return(code)
    
    def search(self, depart, arrive, date_from, date_to, max_price):
        search_ep = f"{self.TEQUILA_ENDPOINT}/v2/search"
        
        parameters = {
            "fly_from": depart,
            "fly_to": arrive,
            "date_from": date_from,
            "date_to": date_to,
            "price_to": max_price,
            "curr": self.currency,
            "nights_in_dst_from": self.min_nights,
            "nights_in_dst_to": self.max_nights,
            "sort": "price",
            "max_stopovers": 3
        }
        
        response = requests.get(url=search_ep, headers=self.HEADERS, params=parameters)
        return(response.json())