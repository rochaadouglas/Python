#Recebe uma matriz quadrada e retorna um valor lógico indicando se ela é ou não simétrica. Uma matriz é simétrica caso, para toda linha l e coluna c: M[l][c] = M[c][l].

def symmetricMatrix(matrix):
    for line in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[line][col] != matrix[col][line]:
                return False
    return True

m = [[1, 2, 3], [2, 4, 5], [3, 4, 9]]
test = symmetricMatrix(m)
print(test)