from flask import Flask, request, jsonify, render_template
from logic import game, pos, reset_jogo
import os

app = Flask(__name__)

@app.route('/')
def index():
    reset_jogo()
    return render_template("index.html")

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    jogador = data.get("jogador")
    posicao = data.get("posicao")
    dificuldade = data.get("dificuldade")
    modo = data.get("modo")

    resultado = game(jogador, posicao, dificuldade, modo)
    return jsonify({"tabuleiro": pos, "resultado": resultado})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)