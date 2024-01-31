# Recebe uma matriz numérica com três colunas (não é necessário verificar a quantidade de colunas) e retorna uma nova matriz com as seguintes modificações na matriz de entrada: a) 1a coluna: multiplicar todos os elementos da desta coluna por 10; b) 2a coluna: calcular o fatorial de cada elemento desta coluna; c) 3a coluna: o módulo de cada elemento desta coluna. Para o cálculo do fatorial, utilize a função factorial do módulo math e para a obtenção do módulo, utilize a função abs incluída no próprio python.

# Receive a numeric array with three columns (it doesn't necessary to check the amoun of columns) and return a new array with some modifications:a) first colum: multiply all elements in the column by 10; b) second column: calculate the factorial of each element in this column; c) third column:the module of each element in this column. for the factorial calculate, use the factorial function from math module and to obtention the module, use the function abs from Python
from math import factorial
def modifiedMatrix(matrix):
    size = len(matrix)
    line = 0
    new_matrix = []
    while line < size:
        amount_col = len(matrix[line])
        col = 0
        new_list = []
        while col < amount_col:
            element = matrix[line][col]
            if col == 0:
                element = element * 10
            elif col == 1:
                element = factorial(element)
            elif col == 2:
                if element < 0:
                    element = element * -1
            col += 1
            new_list.append(element)
        line += 1
        new_matrix.append(new_list)
    return new_matrix

m = [[1, 2, 3], [4, 5, -6], [7, 8, -9]]
test = modifiedMatrix(m)
print(test)