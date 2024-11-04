import random
import math

pos = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

jogar = input("Vamos iniciar ? s/n \n")
pvp = input("São 2 jogadores ? s/n \n")

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
    # Define todas as combinações de vitória
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]
    for combo in win_combinations:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] == jogador:
            return True
    return False

def venceu(jogador):
    if pos[0] == pos[1] == pos[2] == jogador:
        return True
    elif pos[3] == pos[4] == pos[5] == jogador:
        return True
    elif pos[6] == pos[7] == pos[8] == jogador:
        return True
    elif pos[0] == pos[3] == pos[6] == jogador:
        return True
    elif pos[1] == pos[4] == pos[7] == jogador:
        return True
    elif pos[2] == pos[5] == pos[8] == jogador:
        return True
    elif pos[0] == pos[4] == pos[8] == jogador:
        return True
    elif pos[2] == pos[4] == pos[6] == jogador:
        return True
    else:
        return False

def empate():
    return all(pos[i] in ["X", "O"] for i in range(9))

def jog_1():
    while True:
        jog_1 = input("Jogador 1, escolha o numero de uma posição\n")
        if jog_1.isdigit() and pos[int(jog_1) - 1] not in ["X", "O"]:
            pos[int(jog_1) - 1] = "X"
            break
        else: print("Digite um numero valido e disponivel")
    print(tabuleiro())
    return venceu("X")
        
    
def jog_2():
    while True:
        jog_2 = input("Jogador 2, escolha o numero de uma posição\n")
        if jog_2.isdigit() and pos[int(jog_2) - 1] not in ["X", "O"]:
            pos[int(jog_2) - 1] = "O"
            break
        else: print("Digite um numero valido")
    print(tabuleiro())
    return venceu("O")
    
def jog_ia_facil():
    while True:
        jog_ia = random.randint(1, 9)
        if pos[jog_ia - 1] not in ["X", "O"]:
            pos[jog_ia - 1] = "O"
            break
    print(tabuleiro())
    return venceu("O")

def jog_ia_medio():

    for a, b, c in [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]:
        if pos[a] == pos[b] == "O" and pos[c] not in ["X", "O"]:
            pos[c] = "O"
            print(tabuleiro())
            return venceu("O")
        elif pos[a] == pos[c] == "O" and pos[b] not in ["X", "O"]:
            pos[b] = "O"
            print(tabuleiro())
            return venceu("O")
        elif pos[b] == pos[c] == "O" and pos[a] not in ["X", "O"]:
            pos[a] = "O"
            print(tabuleiro())
            return venceu("O")

    for a, b, c in [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]:
        if pos[a] == pos[b] == "X" and pos[c] not in ["X", "O"]:
            pos[c] = "O"
            print(tabuleiro())
            return venceu("O")
        elif pos[a] == pos[c] == "X" and pos[b] not in ["X", "O"]:
            pos[b] = "O"
            print(tabuleiro())
            return venceu("O")
        elif pos[b] == pos[c] == "X" and pos[a] not in ["X", "O"]:
            pos[a] = "O"
            print(tabuleiro())
            return venceu("O")
    
    while True:
        jog_ia = random.randint(1, 9)
        if pos[jog_ia - 1] not in ["X", "O"]:
            pos[jog_ia - 1] = "O"
            break

    print(tabuleiro())
    return venceu("O")

# Função Minimax ajustada para o seu caso
def minimax(b, depth, is_maximizing):
    if venceu_otimizada(b, 'O'):
        return 1  # Vitória da IA
    elif venceu_otimizada(b, 'X'):
        return -1  # Vitória do jogador
    elif empate():
        return 0  # Empate

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] not in ["X", "O"]:  # Agora verifica se está livre
                original_value = b[i]
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = original_value
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] not in ["X", "O"]:  # Agora verifica se está livre
                original_value = b[i]
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = original_value
                best_score = min(score, best_score)
        return best_score

# Função de jogada da IA no modo difícil
def jog_ia_dificil():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if pos[i] not in ["X", "O"]:
            original_value = pos[i]
            pos[i] = 'O'
            score = minimax(pos, 0, False)
            pos[i] = original_value
            if score > best_score:
                best_score = score
                best_move = i
    pos[best_move] = 'O'
    print(tabuleiro())
    return venceu_otimizada(pos, "O")

def jogar():
    while jogar == "s":
        pos = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if pvp == "s":
            print(tabuleiro())
            for i in range(9):
                if i % 2 == 0:
                    if jog_1():
                        print("Jogador 1 venceu")
                        break
                else:  
                    if jog_2():
                        print("Jogador 2 venceu")
                        break
            if i == 8: print("Deu velha")
            jogar = input("Jogar novamente ? s/n \n")
        else: 
            while True:
                print("""Escolah a dificuldade:
1. facil
2. medio
3. Dificil
4. sair""")
                dificuldade = input()
                if dificuldade == "4":
                    break

                match dificuldade:
                    case "1": 
                        "facil"
                        print(tabuleiro())
                        for i in range(9):
                            if i % 2 == 0:
                                if jog_1():
                                    print("O Jogador venceu!!")
                                    break
                            else:
                                if jog_ia_facil():
                                    print("A IA facil venceu")
                                    break
                            if i == 8: print("Deu velha")
                        jogar = input("Jogar novamente ? s/n \n")
                        break

                    case "2":
                        "medio"
                        print(tabuleiro())
                        for i in range(9):
                            if i % 2 == 0:
                                if jog_1():
                                    print("O Jogador venceu!!")
                                    break
                            else:
                                if jog_ia_medio():
                                    print("A IA medio venceu")
                                    break
                            if i == 8: print("Deu velha")
                        jogar = input("Jogar novamente ? s/n \n")
                        break

                    case "3":
                        "dificil"
                        print(tabuleiro())
                        for i in range(9):
                            if i % 2 == 0:
                                if jog_1():
                                    print("O Jogador venceu!!")
                                    break
                            elif jog_ia_dificil():
                                print("A IA dificil venceu")
                                break
                            if i == 8: print("Deu velha")
                        jogar = input("Jogar novamente ? s/n \n")
                        break

                    case _:
                        print("Digite um numero valido")
                        break
    else : print("beleza, flw")