# Recebe uma quantidade de linhas e outra de colunas e retorna uma matriz com todos os elementos com valor 0, a matriz resultante tem as dimensões informadas pelos parâmetros.

# Receive an amount of line and column and return a matrix with all elements with value 0, the resulting matrix have dimensions reported by user.
def newMatrix(line, column):
    size = line
    first_line = 0
    new_matrix = []
    while first_line < size:
        amount_col = column
        first_col = 0
        new_list = []
        while first_col < amount_col:
            element = 0
            new_list.append(element)
            first_col += 1
        new_matrix.append(new_list)
        first_line += 1
    return new_matrix

test = newMatrix(2, 2)
print(test)