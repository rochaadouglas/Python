#Obtenha um valor numérico inteiro, maior do que 0, e calcule o produtório de 1 até o valor informado pelo usuário. Exiba o resultado do produtório e também informe se o resultado é par ou ímpar.
num = int(input('Report your number to the producer: '))
cont = 1
sum = cont + 1
while cont < num:
    sum = cont * sum
    cont += 1