# Recebe uma matriz numérica e retorna quantos elementos da matriz são números primos.

# Receive a numeric matrix and return how many alements of matrix are prime numbers.
from function_cousin import cousin_number
def cousinNumber(matrix):
    size = len(matrix)
    line = 0
    sum = 0
    while line < size:
        amount_col = len(matrix[line])
        col = 0
        while col < amount_col:
            element = matrix[line][col]
            cousin = cousin_number(element)
            if cousin == True:
                sum = sum + 1
            col += 1
        line += 1
    return sum

m = [[2, 4, 9], [1, 5, 11], [34, 7, 10]]
test = cousinNumber(m)
print(test)