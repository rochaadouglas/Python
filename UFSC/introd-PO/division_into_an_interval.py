# Obtenha um valor inteiro no intervalo entre 1 e 9 (inclusive) e conte quantos números são divisíveis pelo valor informado pelo usuário, dentro do intervalo de 1 a 1.000 (inclusive). Caso o usuário entre com um valor fora do intervalo de 1 a 9, avise-o e solicite novamente sua entrada. Solicite a entrada até que o valor seja válido ou que ele entre com o número 0 (nesse caso o programa encerra sem realizar o cálculo).

# Obtain an integer value between 1 and 9 and add how many numbers are divisible by the value entered by the user, in the range from 1 to 1000. If the user input value are wrong, warn him and request your input again. Request the input until a valid value or that he inputs with a number 0 (at this case, the program finish and it doesn't make the sum).
num = int(input('Number: '))
count = 1
while num != 0 and num < 1 or num > 9:
    num = int(input('Write again: '))
    count += 1
    if num == 0:
        print('END')
if num >= 1 and num <= 9:
    cont_integ = 1
    sum = 0
    while cont_integ <= 1000:
        mult = cont_integ % num
        if mult == 0:
            sum = sum + 1
        cont_integ += 1
    print(sum)