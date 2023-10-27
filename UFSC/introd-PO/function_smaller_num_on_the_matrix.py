#Recebe uma matriz numérica e retorna uma lista contendo qual o menor elemento da matriz e sua respectiva posição (linha e coluna)

def smallerNum(matrix):
    size = len(matrix)
    line = 0
    smaller = matrix[0][0]
    new_list = []
    while line < size:
        col = 0
        amount_col = len(matrix[line])
        while col < amount_col:
            element = matrix[line][col]
            if element < smaller:
                smaller = element
            col += 1
        line += 1
    new_list.append(smaller)
    return new_list

m = [[1, 6, 5], [23, 5, 10], [9, 4, 10]]
test = smallerNum(m)
print(test)