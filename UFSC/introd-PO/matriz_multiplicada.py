'''Recebe uma matriz numérica e retorna uma nova matriz onde todos os elementos devem ser multiplicados por 10, com exceção da diagonal principal, onde todos os elementos devem ser 0.'''

def retornaMult(matriz):
    tam = len(matriz)
    ind_linha = 0
    nova_matriz = []
    while ind_linha < tam:
        qtcoluna = len(matriz[ind_linha])
        ind_coluna = 0
        nova_linha = []
        while ind_coluna < qtcoluna:
            if ind_linha == ind_coluna:
                nova_linha.append(0)
            else:
                nova_linha.append(matriz[ind_linha][ind_coluna] * 10)
            ind_coluna += 1
        nova_matriz.append(nova_linha)
        ind_linha += 1
    return nova_matriz
       
m = [[1, 2, 3], [5, 6, 7], [1, 2, 3]]
teste = retornaMult(m)
print(teste)