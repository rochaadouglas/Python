# Recebe uma quantidade de linhas, de colunas e um limite (valor inteiro). Retorne uma matriz com todos os elementos produzidos aleatoriamente (números no intervalo de -limite à +limite), a matriz resultante tem as dimensões informadas pelos parâmetros.

# Receive an amount of lines, columns and a limit (integer value). Return a matrix with all of ramdom elements(numbers in interval from - limit until + limit), the resulting matrix has dimentions reported by user.
import random
def randomMatrix(line, column, limite):
    new_matrix = []
    for li in range(line):
        new_list = [random.randint(-limite, limite) for col in range(column)]
        new_matrix.append(new_list)
    return new_matrix

test = randomMatrix(2, 5, 10)
print(test)