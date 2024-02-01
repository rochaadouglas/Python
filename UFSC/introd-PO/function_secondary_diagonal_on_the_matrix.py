# Recebe uma matriz quadrada por parâmetro e retorna Verdadeiro caso todos os elementos da diagonal secundária sejam iguais e Falso caso contrário.

# Receive a square array by parameter and return True value if all of elements from secondary diagonal are same and False if it isn't.
def trueorfalse(matrix):
    line = 0
    size = len(matrix)
    col = size - 1
    comp_ele = matrix[line][col]
    while line < size:
        element = matrix[line][col]
        if element != comp_ele:
            return False
        line += 1
        col -= 1
    return True

m = [[1, 2, 3, 3], [1, 2, 3, 4], [1, 3, 3, 4], [3, 2, 3, 4]]
test = trueorfalse(m)
print(test)