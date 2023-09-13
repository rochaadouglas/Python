#Obtenha uma quantidade de números a serem lidos via entrada do usuário (qt). Em seguida, obtenha essa quantidade de números (qt) via entrada e, ao final, exiba o somatório dos fatoriais dos números lidos.
#Get a amount of number to be read with user input. Next, make the factorial of the number and show to user the sum of the factorial result.
amount_num = int(input('Number amount: '))
count = 1
sum_fact = 0
while count <= amount_num:
    num = int(input('Factorial number: '))
    count_fact = num - 1
    mult = num
    while count_fact > 0:
        mult = mult * count_fact
        count_fact -= 1
    sum_fact = sum_fact + mult
    count += 1
print(f'The sum of the factorials is: {sum_fact}')