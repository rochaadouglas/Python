'''Recebe uma matriz e retorna uma nova lista com a quantidade linhas e colunas dessa matriz. Caso a matriz tenha alguma linha cuja quantidade de colunas seja diferente da primeira, retorne vazio. Assim, a lista de retorno terá sempre duas dimensões.'''

def retornaLista(matriz):
    tam = len(m)
    linha = 0
    lista = []
    while linha < tam:
        qtcoluna = len(m[linha])
        coluna = 0
        while coluna < qtcoluna:
            if len(qtcoluna) == len(qtcoluna):
                elemento = m[linha][coluna]
                lista.append(elemento)
            coluna += 1
        linha += 1
    return lista


m = [[12, 2, 4, 34], [45, 3, 5, 1]]    #2 linhas 4 colunas
teste = retornaLista(m)
print(teste)