#Anime , Facil
import requests

parameters = {
    "amount": 10,
    "type": "multiple",
}

response = requests.get("https://opentdb.com/api.php?amount=10&category=31&difficulty=easy&type=multiple", params=parameters)
response.raise_for_status()
data = response.json()
ronda_2 = data["results"]