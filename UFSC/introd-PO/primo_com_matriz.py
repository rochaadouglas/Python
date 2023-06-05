'''5. Recebe uma matriz numérica e retorna quantos elementos da matriz são números primos.'''

def primo(numero):
    num = numero
    cont = 1
    soma = 0
    while cont <= num:
        if num % cont == 0:
            soma = soma + 1
        cont += 1
    if soma > 2:
        return False
    else:
        return True
num = 10
teste = primo(num)
print(teste)

'''-----------------------------------------------------------------------------'''

'''from e_primo import primo

def ePrimo(matriz):
    tam = len(m)
    linha = 0
    qtprimos = 0
    while linha < tam:
        qtcoluna = len(m[linha])
        coluna = 0
        while coluna < qtcoluna:
            elemento = m[linha][coluna]
            if primo(elemento):
                qtprimos = qtprimos + 1
            coluna += 1
        linha += 1
    return qtprimos
   
m = [[0, 3, 8], [12, 13, 15], [22, 25, 29]]
teste = ePrimo(m)
print(teste)'''