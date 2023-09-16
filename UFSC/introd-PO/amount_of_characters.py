#Obtenha um número inteiro maior do que 0, esse número indica a quantidade de caracteres que serão exibidos diretamente (na mesma linha, separados por espaço). Os caracteres exibidos são A, B e C, nessa ordem. A cada 3 caracteres A mostrados, troca-se para B, após 3 B’s, troca-se para o C e, finalmente, após 3 C’s, o programa volta a exibir A e o ciclo continua.
#Get a integer number better than 0, it indicates the number of characters that will be show directly (in the same line). The characters are: A, B, C at this order. Each three character A played, it changes to B and each three characters B played, it changes to C. When arriving to C, return for A and continue the cycle (looping).
amount = int(input('Report the number of character: '))
count = 0
letter = 'A'
count_charac = 0
while count < amount:
    print(f'{letter}', end=' ')
    count_charac += 1
    if count_charac == 3:
        if letter == 'A':
            letter = 'B'
        elif letter == 'B':
            letter = 'C'
        else:
            letter = 'A'
        count_charac = 0
    count += 1