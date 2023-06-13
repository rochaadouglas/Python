'''Recebe uma matriz e retorna uma nova lista com a quantidade linhas e colunas dessa matriz. Caso a matriz tenha alguma linha cuja quantidade de colunas seja diferente da primeira, retorne vazio. Assim, a lista de retorno terá sempre duas dimensões.'''

def retornaLista(matriz):
    tam = len(m)
    linha = 0
    referencia = len(matriz[0])
    while linha < tam:
        qtcoluna = len(matriz[linha])
        if qtcoluna != referencia:
            return []
        linha += 1
    return [linha, referencia]
   
m = [[2, 4, 7], [10, 32, 3], [1]]
teste = retornaLista(m)
print(teste)