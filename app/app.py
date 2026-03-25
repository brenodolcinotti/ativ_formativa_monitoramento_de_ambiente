from flask import Flask, render_template
import requests

app = Flask(__name__)

def ler_dados():
    channel_id = 3313549
    read_api_key = "SZYRHJ8QYP4AM2GU"

    url = f"https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={read_api_key}&results=10"

    response = requests.get(url)
    data = response.json()

    registros = []

    if 'feeds' in data:
        for item in data['feeds']:
            registros.append({
                "temperatura": item.get("field1"),
                "umidade": item.get("field2"),
                "data": item.get("created_at")
            })

    return registros

@app.route("/")
def index():
    registros = ler_dados()

    if registros:
        temp = registros[-1]["temperatura"]
        umidade = registros[-1]["umidade"]
    else:
        temp = "--"
        umidade = "--"

    return render_template(
        "index.html",
        temp=temp,
        umidade=umidade,
        registros=registros,
        quantidade=len(registros)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)