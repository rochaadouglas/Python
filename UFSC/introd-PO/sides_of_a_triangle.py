#Obtenha três valores numéricos via entrada do usuário, representando os tamanhos dos lados de um triângulo. Apresente uma mensagem informando se o triângulo é eqüilátero (possui 3 lados iguais), isósceles (possui dois lados iguais) ou escaleno (não possui lados iguais). Caso algum dos tamanhos seja negativo, ou não obedecerem a condição de existência de um triângulo, avise o usuário e não faça a verificação do tipo do triângulo.

first_side = float(input('Report the first side of the triangle: '))
second_side = float(input('Report the second side of the triangle: '))
third_side = float(input('Report the third side of the triangle: '))
sum = first_side + second_side
if third_side < first_side and third_side < second_side or third_side > sum:
    print('You do not have a triangle.')