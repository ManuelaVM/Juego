# _____________________________________________________________________________
# Las preguntas fueron obtenidas de esta https://opentdb.com/api_config.php
# database de preguntas, la categoria de esta Ronda es Geografia y es facil
# _____________________________________________________________________________
import requests

parameters = {
    "amount": 5,
    "type": "multiple",
}

response = requests.get("https://opentdb.com/api.php?amount=5&category=22&difficulty=easy&type=multiple", params=parameters)
response.raise_for_status()
data = response.json()
ronda_1 = data["results"]




