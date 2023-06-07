'''Recebe uma quantidade de linhas e outra de colunas e retorna uma matriz com todos os elementos com valor 0, a matriz resultante tem as dimensões informadas pelos parâmetros'''

def ElementoZero(qtlinha, qtcoluna):
    linha_atual = 0
    matriz = []
    while linha_atual < qtcoluna:
        novaLinha = [0] * qtlinha
        matriz.append(novaLinha)
        linha_atual += 1
    return matriz
    
teste = ElementoZero(10, 10)
print(teste)