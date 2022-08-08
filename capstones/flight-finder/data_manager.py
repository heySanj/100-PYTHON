import os
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        
        self.SHEETY_ENDPOINT = os.environ.get("SHEETY_FLIGHT_ENDPOINT")
        self.SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
        self.SHEETY_AUTH = {
            "Authorization": f"Bearer {self.SHEETY_TOKEN}"
        }
        self.data = self.get_data()
        
    # Return data from the sheet
    def get_data(self):
        response = requests.get(url=self.SHEETY_ENDPOINT, headers=self.SHEETY_AUTH)
        # print(response.text)
        return response.json()['prices']
    
    # Update rows in the sheet
    def put_data(self, row, column, data):
        
        endpoint = f"{self.SHEETY_ENDPOINT}/{row}"
        
        data = {"price": {
                    column: data,
                    }
                }
                
        response = requests.put(url=endpoint, json=data, headers=self.SHEETY_AUTH)