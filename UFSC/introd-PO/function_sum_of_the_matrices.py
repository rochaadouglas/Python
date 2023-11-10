# Recebe duas matrizes numéricas e retorna uma nova matriz com o somatório de cada elemento delas (soma dos elementos com os mesmos índices). Caso as matrizes não tenham as mesmas dimensões, retorne False. Utilize a função definida no exercício 3 para realizar essa verificação.

from function_test_of_matrix import test_matrix
def sumMatrices(matrix1, matrix2):
    test1 = test_matrix(matrix1)
    test2 = test_matrix(matrix2)
    if test1 == False or test2 == False:
        return False
    new_matrix = []
    size = len(matrix1)
    line = 0
    while line < size:
        amount_col = len(matrix1[line])
        col = 0
        new_list = []
        while col < amount_col:
            sum_ele = matrix1[line][col] + matrix2[line][col]
            new_list.append(sum_ele)
            col += 1
        line += 1
        new_matrix.append(new_list)
    return new_matrix

m1 = [[1, 2], [3, 4]]
m2 = [[1, 2], [3, 2]]
test = sumMatrices(m1, m2)
print(test)