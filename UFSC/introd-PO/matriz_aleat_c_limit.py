'''Recebe uma quantidade de linhas, de colunas e um limite (valor inteiro). Retorne uma matriz com todos os elementos produzidos aleatoriamente (números no intervalo de -limite à +limite), a matriz resultante tem as dimensões informadas pelos parâmetros.'''

import random

def matrizAleatoria(qtlinha, qtcoluna, lim_inferior, lim_superior):
    linha_atual = 0
    matriz = []
    while linha_atual < qtlinha:
        novaLinha = [random.randint(lim_inferior, lim_superior)] *qtcoluna
        matriz.append(novaLinha)
        linha_atual += 1
    return matriz

teste = matrizAleatoria(3, 4, 0, 100)
print(teste)
