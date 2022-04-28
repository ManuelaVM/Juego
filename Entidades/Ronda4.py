#Animales , Medio
import requests

parameters = {
    "amount": 5,
    "type": "multiple",
}

response = requests.get("https://opentdb.com/api.php?amount=5&category=27&difficulty=medium&type=multiple", params=parameters)
response.raise_for_status()
data = response.json()
ronda_4 = data["results"]