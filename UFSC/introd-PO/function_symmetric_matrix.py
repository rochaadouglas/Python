#Recebe uma matriz quadrada e retorna um valor lógico indicando se ela é ou não simétrica. Uma matriz é simétrica caso, para toda linha l e coluna c: M[l][c] = M[c][l].

def symmetricMatrix(matrix):
    size = len(matrix)
    line = 0
    while line < size:
        amount_col = len(matrix[line])
        col = 0
        element_col = matrix[0][1]
        while col < amount_col:
            element_line = matrix[1][0]
            if element_col != element_line:
                return False
            col += 1
        line += 1
    return True

m = [[1, 2, 3], [2, 4, 5], [3, 4, 9]]
test = symmetricMatrix(m)
print(test)