#Obtenha um valor numérico inteiro, maior do que 0, e calcule o produtório de 1 até o valor informado pelo usuário. Exiba o resultado do produtório e também informe se o resultado é par ou ímpar.
num = int(input('Report your number to the producer: '))
cont = 1
sum = 1
next_num = sum + 1
result = 0
while cont < num:
    sum = sum * next_num
    result = sum
    next_num += 1
    cont += 1
print(result)
if result % 2 == 0:
    print('É PAR')