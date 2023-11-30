# O propósito desta atividade é implementar o jogo Ligue4 utilizando os recursos de programação abordados na disciplina. A implementação deve ser realizada na linguagem Python (qualquer versão a partir da 3.7).
# O Ligue4 é jogado por dois jogadores e vence quem conseguir montar uma sequência de 4 peças na horizontal, vertical ou diagonal. A figura a seguir ilustra uma vitória do jogador com as peças vermelhas.
# A cada jogada, o jogador escolhe em qual coluna vai empilhar sua peça. Caso a coluna esteja cheia, o jogador não pode jogar naquela coluna e deve escolher outra. Na figura acima, não é possível jogar na coluna do meio. Os jogadores jogam um de cada vez.
# A sua implementação deve possibilitar que dois jogadores humanos joguem um contra o outro e também que um jogador humano jogue contra o computador.

def mostra_tabuleiro(tabuleiro = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]):
    for e in tabuleiro:
        print()
        for c in e:
            print(f'{c}', end=' |')

#definição do modo de jogo
def modo_de_jogo(adversario):
    jogador = adversario
    if jogador == 'Humano':
        print('Okay')

# verifica se há diagonais, retas ou horizontais
def escolha_coluna(): 
    pass

jogador = input('Jogar contra Humano ou PC?')
print()
mostra_tabuleiro()
#modo_de_jogo(jogador)
