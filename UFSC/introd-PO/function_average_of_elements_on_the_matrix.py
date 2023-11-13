# Recebe uma matriz quadrada por parâmetro e retorna a média dos elementos da diagonal principal.

def average(matrix):
    size = len(matrix)
    line = 0
    sum_ele = 0
    while line < size:
        amount_col = len(matrix[line])
        col = 0
        while col < amount_col:
            element = matrix[line][col]
            if line == col:
                sum_ele = sum_ele + element 
            col += 1
        line += 1
    average_ele = sum_ele / size
    return average_ele

m = [[1, 2, 3, 4],
     [1, 0, 3, 4],
     [1, 2, 11, 4], 
     [1, 2, 3, 10]]
test = average(m)
print(test)