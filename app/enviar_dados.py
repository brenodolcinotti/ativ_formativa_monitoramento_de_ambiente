import requests
import random
import time

API_KEY = "SZYRHJ8QYP4AM2GU"

def enviar_dados(temperatura, umidade):
    try:
        url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={temperatura}&field2={umidade}"
        
        resposta = requests.get(url)

        if resposta.status_code == 200 and resposta.text != "0":
            print("Enviado com sucesso!")
        else:
            print("Falha ao enviar")

        print(f"🌡 Temp: {temperatura} | 💧 Umidade: {umidade}")
        print("Resposta:", resposta.text)
        print("-" * 40)

    except Exception as e:
        print("Erro:", e)


while True:
    temperatura = round(random.uniform(20, 30), 2)
    umidade = round(random.uniform(50, 70), 2)

    enviar_dados(temperatura, umidade)

    time.sleep(10)