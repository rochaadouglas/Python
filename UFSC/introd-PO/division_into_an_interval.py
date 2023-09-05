#Obtenha um valor inteiro no intervalo entre 1 e 9 (inclusive) e conte quantos números são divisíveis pelo valor informado pelo usuário, dentro do intervalo de 1 a 1.000 (inclusive). Caso o usuário entre com um valor fora do intervalo de 1 a 9, avise-o e solicite novamente sua entrada. Solicite a entrada até que o valor seja válido ou que ele entre com o número 0 (nesse caso o programa encerra sem realizar o cálculo).

num = int(input('Numero: '))
cont = 1
while num < 1 or num > 9:
    num = int(input('Numero de novo: '))
    cont += 1
    if num == 0:
        print('FIM DO PROGRAMA')
    elif num >= 1 and num <= 9:
        cont_inter = 1
        sum = 0
        while cont_inter <= 20:
            mult = cont_inter % num
            if mult == 0:
                sum = sum + 1
            cont_inter += 1
        print(sum)