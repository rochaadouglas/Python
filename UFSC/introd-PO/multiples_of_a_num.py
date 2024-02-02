# Apresente os múltiplos de um número em ordem crescente. Obtenha, via entrada do usuário, o número o qual deseja-se ver os múltiplos e o total de múltiplos a apresentar. Inicie a apresentação a partir do 1.

# Print the multiples of a number in ascending order. Getting by user input the number what it want to see the multiples and the total of multiples to show. Start the showing from 1.
num = int(input('Report your number: '))
total_multiples = int(input('How many multiples do you want: '))
cont = 1
while cont <= total_multiples:
    result = num * cont
    cont += 1
    print(f'{result} is a multiple of {num}.')