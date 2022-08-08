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
    
    # Return the city code of input city
    def get_city_code(self, city: str) -> str:
        location_ep = f"{self.TEQUILA_ENDPOINT}/locations/query"
        
        parameters = {
            "term": city
        }
        
        response = requests.get(url=location_ep, headers=self.HEADERS, params=parameters)
        code = response.json()['locations'][0]['code']
                
        return(code)