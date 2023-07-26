def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-----")

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if all(posicao == jogador for posicao in linha):
            return True

    # Verificar colunas
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogo_acabou = False

    while not jogo_acabou:
        exibir_tabuleiro(tabuleiro)
        print("Vez do jogador", jogador_atual)

        linha = int(input("Digite o número da linha (0, 1 ou 2): "))
        coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            if verificar_vitoria(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print("Jogador", jogador_atual, "venceu!")
                jogo_acabou = True
            elif all(posicao != " " for linha in tabuleiro for posicao in linha):
                exibir_tabuleiro(tabuleiro)
                print("O jogo empatou!")
                jogo_acabou = True
            else:
                jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Posição inválida. Tente novamente.")

jogar_jogo_da_velha()