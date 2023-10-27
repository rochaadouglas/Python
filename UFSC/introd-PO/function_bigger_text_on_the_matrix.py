#Recebe uma matriz contendo textos e retorna qual o maior texto armazenado na matriz.

def biggerText(matrix):
    size = len(matrix)
    line = 0
    bigger = ''
    while line < size:
        col = 0
        amount_col = len(matrix[line])
        while col < amount_col:
            element = matrix[line][col]
            if len(element) > len(bigger):
                bigger = element
            col += 1
        line += 1
    return bigger

m = [['dodo', 'hehe'], ['douglas', 'ver'], ['dez', 'um']]
test = biggerText(m)
print(test)