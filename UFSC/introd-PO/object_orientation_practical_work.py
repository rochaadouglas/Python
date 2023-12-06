# informo que recebi ajudas para a construção de alguns métodos do programa.

import random


class Tabuleiro:
    # Cria uma matriz 6x7 (6 linhas e 7 colunas) representando o tabuleiro vazio.
    def __init__(self):
        self.tabuleiro = [[' ' for i in range(7)] for i in range(6)]

    # Exibe o tabuleiro
    def exibir_tabuleiro(self):
        for linha in self.tabuleiro:
            print('|'.join(linha))
        print('-' * 29)

    # Realiza a jogada de um jogador em uma coluna
    # Percorre as linhas da coluna, de baixo para cima. Quando encontra a primeira posição vazia, preenche com a peça do jogador (X ou O). Retorna True se a jogada for bem-sucedida e False se a coluna estiver cheia
    def realizar_jogada(self, coluna, jogador):
        for i in range(6):
            linha = 5 - i
            if self.tabuleiro[linha][coluna] == ' ':
                self.tabuleiro[linha][coluna] = jogador.peca
                return True
        return False

    # Verificar se o jogador atual venceu o jogo.
    # Verificação de vitória. Analisando as linhas, colunas e diagonais do tabuleiro para encontrar sequências de 4 peças iguais do jogador.
    def verificar_vitoria(self, jogador):
        for linha in self.tabuleiro:
            count = 0
            for elemento in linha:
                if elemento == jogador.peca:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0
        return False

        # Verificar vitória na vertical
        for coluna in self.tabuleiro[0]:
            count = 0
            for linha in self.tabuleiro:
                if linha[coluna] == jogador.peca:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0
        return False

        # Verificar vitória na diagonal
        for i in range(3, 6):
            for j in range(4):
                # Verificar diagonal descendente \
                diagonal_descendente = (self.tabuleiro[i][j] == jogador.peca and self.tabuleiro[i - 1][j + 1] == jogador.peca and self.tabuleiro[i - 2][j + 2] == jogador.peca and self.tabuleiro[i - 3][j + 3] == jogador.peca)

            # Verificar diagonal ascendente /
                diagonal_ascendente = (self.tabuleiro[i][j + 3] == jogador.peca and self.tabuleiro[i - 1][j + 2] == jogador.peca and self.tabuleiro[i - 2][j + 1] == jogador.peca and self.tabuleiro[i - 3][j] == jogador.peca)
                if diagonal_descendente or diagonal_ascendente:
                    return True

        return False

    # Verificar se o tabuleiro está cheio.
    # Usa a função all para verificar se todas as células do tabuleiro estão preenchidas, ou seja, se não há mais espaços vazios.
    def tabuleiro_cheio(self):
        for linha in self.tabuleiro:
            if ' ' in linha:
                return False
        return True

# Atribui um nome e uma peça (X ou O) ao jogador.


class Jogador:
    def __init__(self, nome, peca):
        self.nome = nome
        self.peca = peca

# Inicializa um objeto Jogo.


class Jogo:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.jogadores = []

    # Adiciona um jogador à lista de jogadores.
    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    # Solicita uma jogada ao jogador
    def realizar_jogada_jogador(self, jogador):
        coluna = int(input(f"{jogador.nome}, escolha a coluna (0-6) para fazer sua jogada: "))
        if 0 <= coluna <= 6 and self.tabuleiro.realizar_jogada(coluna, jogador):
            return True
        else:
            print("Jogada inválida. Tente novamente.")
        return False

    # Realiza uma jogada aleatória para o jogador computador.
    def realizar_jogada_computador(self):
        coluna = random.randint(0, 6)
        while not self.tabuleiro.realizar_jogada(coluna, self.jogadores[1]):
            coluna = random.randint(0, 6)
        return True

    # Inicia o jogo.
    def iniciar_jogo(self):
        print("Escolha o modo de jogo:")
        print("1. Humano vs Computador")
        print("2. Humano vs Humano")

        modo = int(
            input("Digite o número correspondente ao modo de jogo desejado: "))

        jogador1 = Jogador(input("Digite o nome do Jogador 1: "), 'X')
        jogador2 = Jogador("Computador" if modo == 2 else input(
            "Digite o nome do Jogador 2: "), 'O')

        self.adicionar_jogador(jogador1)
        self.adicionar_jogador(jogador2)
        self.tabuleiro.exibir_tabuleiro()

        while True:
            for jogador in self.jogadores:
                if jogador == jogador1 or (jogador == jogador2 and modo == 2):
                    while not self.realizar_jogada_jogador(jogador):
                        pass
                else:
                    self.realizar_jogada_computador()

                self.tabuleiro.exibir_tabuleiro()
                if self.tabuleiro.verificar_vitoria(jogador):
                    print(f"Parabéns, {jogador.nome}! Você venceu!")
                    return
                elif self.tabuleiro.tabuleiro_cheio():
                    print("Empate! O tabuleiro está cheio.")
                    return


jogo = Jogo()
jogo.iniciar_jogo()
