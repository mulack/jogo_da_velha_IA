from flask import Flask, render_template, jsonify, request
import Jogo_da_velha_IA

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jogada', methods=['POST'])
def jogada():
    data = request.get_json()
    posicao = data['posicao']
    jogador = data['jogador']
    
    # Realiza a jogada
    Jogo_da_velha_IA.pos[int(posicao) - 1] = jogador
    resultado = Jogo_da_velha_IA.verificar_vitoria()
    
    # IA joga se o jogo não terminou
    if resultado is None:
        resultado = Jogo_da_velha_IA.jogada_ia_facil()
    
    return jsonify({'tabuleiro': Jogo_da_velha_IA.pos, 'resultado': resultado})

@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    Jogo_da_velha_IA.reiniciar_jogo()
    return jsonify({'tabuleiro': Jogo_da_velha_IA.pos})

if __name__ == '__main__':
    app.run(debug=True)
