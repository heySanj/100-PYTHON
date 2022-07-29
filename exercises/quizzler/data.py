import requests
import json

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status() # Raise exceptions
data = response.json()

# print(json.dumps(data, indent=4, sort_keys=True))

question_data = data['results']