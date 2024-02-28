# Obtenha dois números inteiros os quais representam o limite inferior e o superior de um somatório. Caso o limite inferior seja de fato menor ou igual ao superior, calcule e apresente o resultado do somatório. Caso contrário avise o usuário e não realize o cálculo.

# Get two integer numbers that representing the inferior and the superior limit of a somatory. If the inferior limit is smaller or same the superior, calculate and show the result of sum. If not, report to user and don't make the calculate.
bottom_num = int(input('Report the bottom number: '))
higher_num = int(input('Report the higher number: '))
sum = bottom_num
cont = bottom_num + 1
while cont <= higher_num:
    sum = sum + cont
    cont += 1
print(sum)