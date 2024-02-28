# Recebe uma matriz numérica e informe para o usuário quais linhas e colunas possuem somente valores negativos.

# Receive a numeric matrix and report to user what line and column that have only negative values.
def negativeValue(matrix):
    size = len(matrix)
    line = 0
    while line < size:
        amount_col = len(matrix[line])
        col = 0
        while col < amount_col:
            element = matrix[line][col]
            if element < 0:
                print(f'line {line}, column {col} negative value')
            col += 1
        line += 1

m = [[1, 2, 3], [2, -5, 5], [10, 33, -1]]
test = negativeValue(m)