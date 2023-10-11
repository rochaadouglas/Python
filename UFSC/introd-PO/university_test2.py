#Desenvolva um programa que leia um número inteiro maior do que 1 (não é necessário verificar) via entrada do usuário, e exiba uma figura conforme os exemplos abaixo. Note que a entrada do usuário determina a altura e largura da figura. 
#Sugestão: crie e utilize uma função chamada mostraLinha, a qual recebe uma quantidade de espaços e uma quantidade de números e apenas mostra os espaços seguidos dos números em uma única linha. Essa função não precisa ter retorno.

def mostraEspa(qt):
    cont = 1
    while cont <= qt:
        print(' ', end='')
        cont += 1

def mostraNum(fim):
    cont = 1
    while cont <= fim:
        print(cont, end='')
        cont += 1
        
entrada = 4
la = 1
cont_num = 1
qtespa = entrada - 1
while la <= entrada:
    mostraEspa(qtespa)
    mostraNum(cont_num)
    mostraEspa(qtespa)
    la += 1
    cont_num += 2
    qtespa -= 1
    print()

cont_num2 = entrada+1
la2 = entrada - 1
qtespa = 1
while la2 > 0:
    mostraEspa(qtespa)
    mostraNum(cont_num2)
    mostraEspa(qtespa)
    la2 -= 1
    cont_num2 -= 2
    qtespa += 1
    print()