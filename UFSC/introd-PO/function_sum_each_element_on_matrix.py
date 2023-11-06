#Recebe uma matriz numérica quadrada (verifique utilizando a função anterior) e retorne uma lista com o somatório dos elementos de cada coluna.

from function_square_matrix import squareMatrix
def sumElement(matrix):
    size = len(matrix)
    line = 0
    new_list = []
    matri = squareMatrix(matrix)
    if matri == True:
        while line < size:
            amount_col = len(matrix[line])
            col = 0
            sum_elem = 0
            while col < amount_col:
                element = matrix[line][col]
                sum_elem = sum_elem + element
                col += 1
            new_list.append(sum_elem)
            line += 1
        return new_list
    else:
        return False

m = [[2, 4, 0], [33, 90, 5], [4, 8, 9]]
test = sumElement(m)
print(test)