# Recebe uma matriz numérica e retorna uma lista contendo qual o menor elemento da matriz e sua respectiva posição (linha e coluna).

# Receive a numeric matrix and return a list containing what the smallest element of the matrix and your respective position.
def smallerNum(matrix):
    size = len(matrix)
    line = 0
    smaller = matrix[0][0]
    new_list = []
    ind_line = 0
    ind_col = 0
    while line < size:
        col = 0
        amount_col = len(matrix[line])
        while col < amount_col:
            element = matrix[line][col]
            if element < smaller:
                smaller = element
                ind_line = line
                ind_col = col
            col += 1
        line += 1
    new_list.append(smaller)
    new_list.append(ind_line)
    new_list.append(ind_col)
    return new_list

m = [[10, 6, 5], [23, 5, 10], [9, 4, 10]]
test = smallerNum(m)
print(test)