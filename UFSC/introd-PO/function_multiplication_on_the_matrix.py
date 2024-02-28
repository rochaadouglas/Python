# Recebe uma matriz numérica e retorna uma nova matriz onde todos os elementos devem ser multiplicados por 10, com exceção da diagonal principal, onde todos os elementos devem ser 0.

# Receive a numeric matrix and return a new matrix where all elements are be multiplicate for 10, except the principal diagonal, where all elements are be 0.
def multiplicMatrix(matrix, num):
    mult = num
    size = len(matrix)
    line = 0
    new_matrix = []
    while line < size:
        amount_col = len(matrix[line])
        col = 0
        new_list = []
        while col < amount_col:
            mult_ele = matrix[line][col] * mult
            if line == col:
                mult_ele = matrix[line][col] * 0
            new_list.append(mult_ele)
            col += 1
        line += 1
        new_matrix.append(new_list)
    return new_matrix

test = multiplicMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10)
print(test)