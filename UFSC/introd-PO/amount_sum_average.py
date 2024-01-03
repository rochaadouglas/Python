#Obtenha números inteiros quaisquer via entrada do usuário até que o usuário entre com o número 0. Informe a quantidade números digitados, o somatório e a média dos números.

#Get any integer numbers with user input until the user input with number 0. Inform the amount of number, sum of number and average of number.
num = int(input('Report your number: '))
cont = 0
amount = 0
sum = num
average = 0
while num != 0:
    num = int(input('Report your number: '))
    amount = amount + 1
    sum = sum + num
    average = sum / amount
    cont += 1
print(f'Amount of number: {amount}') #quantidade
print(f'Sum of number: {sum}') #soma
print(f'Average of number: {average:.1f}') #média 