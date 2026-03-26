from flask import Flask, render_template, redirect
import requests
import mysql.connector
import random

app = Flask(__name__)

# 🔐 SUA API KEY (WRITE)
WRITE_API_KEY = "SZYRHJ8QYP4AM2GU"

# 🔹 CONEXÃO MYSQL
def conectar_mysql():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="monitoramento"
    )

# 🔹 SALVAR NO MYSQL
def salvar_mysql(temp, umidade):
    conn = conectar_mysql()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO dados (temperatura, umidade) VALUES (%s, %s)",
        (temp, umidade)
    )

    conn.commit()
    cursor.close()
    conn.close()

# 🔹 LER DO MYSQL
def ler_mysql():
    conn = conectar_mysql()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM dados ORDER BY id DESC LIMIT 10")
    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados

# 🔹 LER DO THINGSPEAK
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

# 🔹 HOME
@app.route("/")
def index():
    registros = ler_dados()
    mysql_dados = ler_mysql()

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
    quantidade=len(registros),
    mysql_dados=ler_mysql()  # 🔥 FALTAVA ISSO
)

# 🔥 BOTÃO
@app.route("/enviar")
def enviar():
    temp = round(random.uniform(20, 30), 2)
    umidade = round(random.uniform(50, 70), 2)

    # envia para ThingSpeak
    requests.get(
        f"https://api.thingspeak.com/update?api_key={WRITE_API_KEY}&field1={temp}&field2={umidade}"
    )

    # salva no MySQL
    salvar_mysql(temp, umidade)

    return redirect("/")

# 🔥 RUN
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)