# Obtenha um valor numérico inteiro, maior do que 0, e calcule o produtório de 1 até o valor informado pelo usuário. Exiba o resultado do produtório e também informe se o resultado é par ou ímpar.

# Get a integer numeric value  bigger than 0 and calculate the product from 1 until the value reported by user.  Print the product result and inform if it is ever or odd too.
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