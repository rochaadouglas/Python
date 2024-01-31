# Recebe uma matriz numérica e retorna o somatório de todos os elementos da matriz.

# Receve a numeric array and returns the sum of all elements in the array
def matrixSum(matrix):
    size = len(matrix)
    line = 0
    sum = 0
    while line < size:
        col = 0
        amount_col = len(matrix[line])
        while col < amount_col:
            sum = sum + matrix[line][col]
            col += 1
        line += 1
    return sum

m = [[2, 3, 4, 5], [1, 4, 2, 4], [1, 4, 2, 4]]
test = matrixSum(m)
print(test)