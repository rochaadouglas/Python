#Desenvolva um programa que leia um número inteiro maior do que 1 (não é necessário verificar) via entrada do usuário, e exiba uma figura conforme os exemplos abaixo. Note que a entrada do usuário determina a altura e largura da figura. 
# Número de linhas no padrão
qt_linhas = int(input('Informe a quantidade de linhas: '))
ind = 1
while ind <= qt_linhas: #contador da quantidade de linhas
    cont_num = 1
    while cont_num <= ind: #contador dos números da esquerda
        print(cont_num, end='')
        cont_num += 1
    
    cont_carac = 0
    while cont_carac <= (qt_linhas - ind) * 2: #contador de caracter, encontrando o padrão
        print('*', end='')
        cont_carac += 1
    
    cont_num2 = 1
    while cont_num2 <= ind: #contador dos números da direita
        print(cont_num2, end='')
        cont_num2 += 1
    
    print()  # Mova para a próxima linha
    ind += 1