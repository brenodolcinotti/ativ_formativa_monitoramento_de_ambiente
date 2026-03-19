import requests
import random

def enviar_dados():
    temp = round(random.uniform(20, 30), 2)
    umidade = round(random.uniform(50, 80), 2)

    url = "https://api.thingspeak.com/update"
    params = {
        "api_key": "SUA_WRITE_KEY",
        "field1": temp,
        "field2": umidade
    }

    requests.get(url, params=params)
