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
import requests
import json
from datetime import datetime, timedelta




# ---------------------------- GET EXERCISE DATA ------------------------------- # 

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRITIONIX_APPID = os.environ.get("NUTRITIONIX_APPID")

GENDER = "male"
WEIGHT_KG = "102.5"
HEIGHT_CM = "196.00"
AGE = "30"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

headers = {
    "x-app-id": NUTRITIONIX_APPID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0"
}

def get_data(query: str):
    exercise_params = {
        "query": query,
        "gender":GENDER,
        "weight_kg":WEIGHT_KG,
        "height_cm":HEIGHT_CM,
        "age":AGE
    }

    # POST request
    response = requests.post(url=NUTRITIONIX_ENDPOINT, json=exercise_params, headers=headers)
    # print(response.text)
    
    # Print out the JSON Data
    # print(json.dumps(response.json(), indent=4, sort_keys=True))
    exercises = response.json()['exercises']
    
    for exercise in exercises:    
        data = {"workout": {
                        "date": today_date,
                        "time": now_time,
                        "exercise": exercise['name'].title(),
                        "duration": exercise['duration_min'],
                        "calories": int(exercise['nf_calories']),
                    }
                }
        
        post_data(data)
    
    
# ---------------------------- SHEETY ------------------------------- # 

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

SHEETY_AUTH = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

def post_data(data: dict):
    
    # POST request
    response = requests.post(url=SHEETY_ENDPOINT, json=data, headers=SHEETY_AUTH)
    print(response.text)
    
    # Print out the JSON Data
    # print(json.dumps(response.json(), indent=4, sort_keys=True))
    
    
# ---------------------------- EXECUTE ------------------------------- #  

exercise = input("Tell me which exercises you did: ")

get_data(exercise)

