# Recebe uma quantidade de linhas, de colunas e um limite (valor inteiro). Retorne uma matriz com todos os elementos produzidos aleatoriamente (números no intervalo de -limite à +limite), a matriz resultante tem as dimensões informadas pelos parâmetros.

import random
def randomMatrix(line, column, limite):
    new_matrix = []
    for li in range(line):
        new_list = [random.randint(-limite, limite) for col in range(column)]
        new_matrix.append(new_list)
    return new_matrix

test = randomMatrix(2, 5, 10)
print(test)