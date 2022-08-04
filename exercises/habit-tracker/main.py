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
from datetime import datetime, timedelta

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_USER = os.environ.get("PIXELA_USER")


headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}


# ---------------------------- USER SETUP ------------------------------- # 
def create_user():
    user_params = {
        "token": PIXELA_TOKEN,
        "username": PIXELA_USER,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    # POST request
    response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print(response.text)


# ---------------------------- GRAPH SETUP ------------------------------- # 
def create_graph():
    
    PIXELA_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs"
    
    graph_params = {
        "id": "graph1",
        "name": "Study Graph",
        "unit": "minutes",
        "type": "int",
        "color": "ichou"
    }

    # POST request
    response = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=graph_params, headers=headers)
    print(response.text)
    
def post_pixel(graph_id, date, amount: int):
    
    formatted_date = date.strftime("%G%m%d")
    
    PIXELA_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs/{graph_id}"
    
    pixel_params = {
        "date": formatted_date,
        "quantity": f"{amount}"
    }

    # POST request
    response = requests.post(url=PIXELA_PIXEL_ENDPOINT, json=pixel_params, headers=headers)
    print(response.text)
    

def put_pixel(graph_id, date, amount: int):
    
    formatted_date = date.strftime("%G%m%d")
    
    PIXELA_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs/{graph_id}/{formatted_date}"
    
    pixel_params = {
        "quantity": f"{amount}"
    }

    # PUT request
    response = requests.put(url=PIXELA_PIXEL_ENDPOINT, json=pixel_params, headers=headers)
    print(response.text)
    
    
def delete_pixel(graph_id, date):
    
    formatted_date = date.strftime("%G%m%d")
    
    PIXELA_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs/{graph_id}/{formatted_date}"

    # PUT request
    response = requests.put(url=PIXELA_PIXEL_ENDPOINT, headers=headers)
    print(response.text)
    
    
# ---------------------------- EXECUTE ------------------------------- #     

put_pixel("graph1", datetime.now() - timedelta(days = 1), 122)