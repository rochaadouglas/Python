#Obtenha via entrada do usuário um número inteiro positivo qualquer e exiba a tabuada desse número.
#Get with user input a any positive integer number and show the multiplication table of this number.
num = int(input('Report the number for your multiplication table: '))
cont = 1
while cont <= 10:
    result = num * cont
    print(f'{num}x{cont}={result}')
    cont += 1