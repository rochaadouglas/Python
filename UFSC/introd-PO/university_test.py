#Desenvolva um programa com as funções especificadas na letra a) e b) 

#a) Função quantidades - Esta função tem como parâmetro uma lista e um número e retorna quantas vezes o número aparece na lista. Para isso, sua função deve percorrer apenas uma vez o argumento recebido (tampouco é possível percorrer cópias do argumento). Sugestão: nesse caso, o operador in não é necessário e vai dificultar a solução.

#b) Função apenasRepetidos - Esta função tem como parâmetro uma lista e retorna uma nova lista contendo apenas os elementos que repetem-se mais de uma vez na lista recebida. A função também retorna o menor elemento dentre os que repetem-se, essa informação é retornada como o último elemento da lista de retorno. Ambas análises devem ser feitas em uma única estrutura de repetição, ou seja, percorrendo-se o argumento recebido apenas uma vez (tampouco é possível percorrer cópias do argumento). Sugestão: utilize a função da letra a) para verificar se um elemento aparece mais do que uma vez.

def quantidade(lista, num):
    tam = len(lista)
    valor = num
    ind = 0
    soma = 0
    while ind < tam:
        elemento = lista[ind]
        if elemento == valor:
            soma = soma + 1
        ind += 1
    return soma
    
#teste = quantidade([1, 1, 4, 5, 5])
#print(teste)

def apenasRepetidos(lista):
    tam = len(lista)
    ind = 0
    lista_elementos = []
    nova_lista = []
    while ind < tam:
        elemento = lista[ind]
        check = quantidade(lista, elemento)
        if check > 1:
            nova_lista.append(elemento)
        ind += 1
    return nova_lista

lista = [2, 3, 3, 1, 3, 1, 2]
teste = apenasRepetidos(lista)
print(teste)
