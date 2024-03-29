# Recebe uma matriz quadrada por parâmetro e mostra, para o usuário, a matriz da entrada multiplicada pelos elementos da sua diagonal principal. Multiplique todos os elementos de cada linha pelo respectivo elemento da diagonal principal.

# Receive a square matrix by parameter and show it to user the beggin matrix multiplication by elements of your original matrix. Multiplicate all elements of each line by respective elements from principal diagonal.
def mult_ele(matrix):
    size = len(matrix)
    line = 0
    lm = 0
    cm = 0
    new_matrix = []
    while line < size:
        amount_col = len(matrix[line])
        col = 0
        mult = matrix[lm][cm]
        new_list = []
        while col < amount_col:
            element = matrix[line][col]
            mult_ele = element * mult
            col += 1
            new_list.append(mult_ele)
        line += 1
        lm += 1
        cm += 1
        new_matrix.append(new_list)
    return new_matrix

m = [[2, 2, 3, 4],
     [2, 2, 3, 4],
     [3, 2, 3, 4],
     [4, 2, 3, 4]]
test = mult_ele(m)
print(test)