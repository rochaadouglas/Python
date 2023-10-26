#Recebe uma matriz numérica e retorna o somatório de todos os elementos da matriz.

def matrizSum(matriz):
    size = len(matriz)
    line = 0
    sum = 0
    while line < size:
        col = 0
        amount_col = len(matriz[line])
        while col < amount_col:
            sum = sum + matriz[line][col]
            col += 1
        line += 1
    return sum

m = [[2, 3, 4, 5], [1, 4, 2, 4], [1, 4, 2, 4]]
teste = matrizSum(m)
print(teste)