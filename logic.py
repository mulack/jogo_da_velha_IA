import random
import math

# Estado inicial do tabuleiro e configurações de jogo
pos = [" "] * 9
modo_jogo = "pvp"  # "pvp" para jogador vs jogador, ou "ia" para jogar contra a IA
dificuldade_ia = "facil"  # "facil", "medio" ou "dificil"

def tabuleiro():
    return (f"""
        |    |    
      {pos[0]} |  {pos[1]} |  {pos[2]}
    ____|____|____
        |    |
      {pos[3]} |  {pos[4]} |  {pos[5]}
    ____|____|____
        |    |
      {pos[6]} |  {pos[7]} |  {pos[8]}
        |    |
    """)

def venceu_otimizada(b, jogador):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combinations:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] == jogador:
            return True
    return False

def empate():
    return all(pos[i] in ["X", "O"] for i in range(9))

def jog_1(posicao):
    pos[posicao] = "X"
    return venceu_otimizada(pos, "X")

def jog_2(posicao):
    pos[posicao] = "O"
    return venceu_otimizada(pos, "O")

def jog_ia_facil():
    while True:
        jog_ia = random.randint(0, 8)
        if pos[jog_ia] not in ["X", "O"]:
            pos[jog_ia] = "O"
            break
    return venceu_otimizada(pos, "O")

def jog_ia_medio():
    # Tentativa de vitória ou bloqueio
    for a, b, c in [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]:
        if pos[a] == pos[b] == "O" and pos[c] not in ["X", "O"]:
            pos[c] = "O"
            return venceu_otimizada(pos, "O")
        elif pos[a] == pos[c] == "O" and pos[b] not in ["X", "O"]:
            pos[b] = "O"
            return venceu_otimizada(pos, "O")
        elif pos[b] == pos[c] == "O" and pos[a] not in ["X", "O"]:
            pos[a] = "O"
            return venceu_otimizada(pos, "O")
    return jog_ia_facil()  # Se nada funcionar, faz um movimento aleatório

def jog_ia_dificil():
    def minimax(b, depth, is_maximizing):
        if venceu_otimizada(b, 'O'):
            return 1
        elif venceu_otimizada(b, 'X'):
            return -1
        elif empate():
            return 0
        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if b[i] not in ["X", "O"]:
                    b[i] = 'O'
                    score = minimax(b, depth + 1, False)
                    b[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if b[i] not in ["X", "O"]:
                    b[i] = 'X'
                    score = minimax(b, depth + 1, True)
                    b[i] = " "
                    best_score = min(score, best_score)
            return best_score
    
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if pos[i] not in ["X", "O"]:
            pos[i] = 'O'
            score = minimax(pos, 0, False)
            pos[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    pos[best_move] = 'O'
    return venceu_otimizada(pos, "O")

def reset_jogo():
    global pos
    pos = [" "] * 9

# Função principal para o jogo
def game(jogador, posicao, dificuldade=None, modo=None):
    global modo_jogo, dificuldade_ia
    if modo:
        modo_jogo = modo
    if dificuldade:
        dificuldade_ia = dificuldade
    if jogador == "X":
        return jog_1(posicao)
    elif jogador == "O":
        if modo_jogo == "pvp":
            return jog_2(posicao)
        elif modo_jogo == "ia":
            if dificuldade_ia == "facil":
                return jog_ia_facil()
            elif dificuldade_ia == "medio":
                return jog_ia_medio()
            elif dificuldade_ia == "dificil":
                return jog_ia_dificil()
    return None
