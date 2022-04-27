#Mitologia , Medio
import requests

parameters = {
    "amount": 10,
    "type": "multiple",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
ronda_3 = data["results"]