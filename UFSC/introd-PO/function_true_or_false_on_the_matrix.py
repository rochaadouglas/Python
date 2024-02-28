# Recebe uma matriz numérica e um número como parâmetros e retorna um valor lógico informando se ela contém ou não o número informado.

# Receive a numeric matrix and a number as parameter and return a logical value informing if it contening or not the number.
def trueorfalse(matrix, number):
    num = number
    size = len(matrix)
    line = 0
    while line < size:
        amount_col = len(matrix[line])
        col = 0
        while col < amount_col:
            element = matrix[line][col]
            if element == num:
                return True
            col += 1
        line += 1
    return False

test = trueorfalse([[23, 12, 99], [90, 2, 8], [4, 9, 22]], 13)
print(test)