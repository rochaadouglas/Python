#Obtenha uma quantidade de linhas, portanto um número inteiro maior do que 0, via entrada do usuário e exiba um triângulo simples formado pelo caractere * contendo a quantidade de linhas informada pelo usuário.
#Get a number of lines, therefore a integer number batter than 0 by user input, and show a simple triangle formed by caracter "*" containig the number of lines reported by user.
num_lines = int(input('Number of lines for triangle: '))
count_lines = 1
while count_lines <= num_lines:
    count_carac = 1
    carac = '*'
    while count_carac <= count_lines:
        print(f'{carac}', end='')
        carac = '*'
        count_carac += 1
    print()
    count_lines += 1