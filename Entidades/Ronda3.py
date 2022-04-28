#Mitologia , Medio
import requests

parameters = {
    "amount": 5,
    "type": "multiple",
}

response = requests.get("https://opentdb.com/api.php?amount=5&category=20&difficulty=medium&type=multiple", params=parameters)
response.raise_for_status()
data = response.json()
ronda_3 = data["results"]