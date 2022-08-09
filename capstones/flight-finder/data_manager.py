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
        self.price_data = self.get_data("prices")
        self.user_data = self.get_data("users")
        
    # Return data from the sheet
    def get_data(self, sheet: str):
        response = requests.get(url=f"{self.SHEETY_ENDPOINT}/{sheet}", headers=self.SHEETY_AUTH)
        # print(response.text)
        return response.json()[sheet]
    
    # Update rows in the sheet
    def put_data(self, sheet, row, column, data):
        
        endpoint = f"{self.SHEETY_ENDPOINT}/{sheet}/{row}"
        
        data = {sheet[:-1]: {
                    column: data,
                    }
                }
                        
        response = requests.put(url=endpoint, json=data, headers=self.SHEETY_AUTH)
        print(response)
        
    def post_data(self, sheet, data):
        
        endpoint = f"{self.SHEETY_ENDPOINT}/{sheet}"
        
        data = {sheet[:-1]: data}
                
        response = requests.post(url=endpoint, json=data, headers=self.SHEETY_AUTH)
        print(response)