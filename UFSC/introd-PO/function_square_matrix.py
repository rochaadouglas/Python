# Recebe uma matriz numérica e retorna um valor lógico informando se ela é uma matriz quadrada ou não (uma matriz é quadrada caso ela tenha a mesma quantidade de linhas e colunas, exemplos: 5x5 e 10x10).

# Receive a numeric matrix and return a logical value reporting if it is a square matrix or not.
def squareMatrix(matrix):
    size = len(matrix)
    line = 0 
    while line < size:
        amount_col = len(matrix[line])
        col = 0
        sum_col = 0
        while col < amount_col:
            sum_col = sum_col + 1
            if sum_col > size:
                return False
            col += 1
        line += 1
        if sum_col < size:
            return False
    return True
   
#m = [[2, 4, 0], [33, 90, 5], [4, 8, 9]]
#test = squareMatrix(m)
#print(test)
