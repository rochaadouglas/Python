# Recebe uma matriz e retorna uma nova lista com a quantidade linhas e colunas dessa matriz. Caso a matriz tenha alguma linha cuja quantidade de colunas seja diferente da primeira, retorne vazio. Assim, a lista de retorno terá sempre duas dimensões.

def test_matrix(matrix):
    size = len(matrix)
    line = 0
    comp = len(matrix[0])
    new_list = []
    while line < size:
        amoun_col = len(matrix[line])
        col = 0
        while col < amoun_col:
            if amoun_col != comp:
                return False
            col += 1
        line += 1
    new_list.append(line)
    new_list.append(col)
    return True

#m = [[1, 2], [3, 4]]
#test = test_matrix(m)
#print(test)