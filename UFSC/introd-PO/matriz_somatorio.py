'''Recebe duas matrizes numéricas e retorna uma nova matriz com o somatório de cada elemento delas (soma dos elementos com os mesmos índices). Caso as matrizes não tenham as mesmas dimensões, retorne False. Utilize a função definida no exercício 3 para realizar essa verificação.'''

def retornaLista2(matriz):
    tam = len(matriz)
    linha = 0
    referencia = len(matriz[0])
    while linha < tam:
        qtcoluna = len(matriz[linha])
        if qtcoluna != referencia:
            return []
        linha += 1
    return [linha, referencia]

def retornaSoma(matriz, matriz2):
    if len(matriz) != len(matriz2):
        return False
    tam = len(matriz)
    linha = 0
    soma = 0
    nova_matriz = []
    while linha < tam:
        qtcoluna = len(matriz[linha])
        coluna = 0
        while coluna < qtcoluna:
            soma = matriz[linha][coluna] + matriz2[linha][coluna]
            nova_matriz.append(soma)    
            #print(soma2)            
            coluna += 1
        linha += 1
    return [nova_matriz]

m1 = [[2, 3, 1], [2, 5, 3]]
m2 = [[0, 1, 0], [0, 2, 5]]
teste = retornaSoma(m1, m2)
print(teste)