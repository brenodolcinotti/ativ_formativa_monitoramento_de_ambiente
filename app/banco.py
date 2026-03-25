import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="monitoramento"
    )