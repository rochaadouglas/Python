#Recebe uma matriz e a apresenta para o usuário na forma de linhas x colunas, cada elemento separado por um espaço em branco.

def showMatrix(matrix):
    size = len(matrix)
    line = 0
    while line < size:
        col = 0
        amount_col = len(matrix[line])
        while col < amount_col:
            element = matrix[line][col]
            print(f'{element}', end=' ')
            col += 1
        print()
        line += 1

m = [[2, 3, 9], [7, 9, 1], [2, 5, 8]]
test = showMatrix(m)