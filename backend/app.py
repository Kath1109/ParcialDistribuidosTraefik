from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def comercial():
    return "Bienvenido a la API Comercial Pokémon"

@app.route("/legendario")
def legendario():
    return "Has accedido al vuelo legendario Pokémon"

@app.route("/hora")
def hora():
    return f"Hora actual del servidor: {datetime.datetime.now()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
