'''Obtenha três valores numéricos via entrada do usuário, representando os ângulos de um triângulo. Caso a soma dos ângulos internos ultrapasse 180°, avise o usuário e não siga com o programa. A partir dos ângulos, classifique o triângulo informado de acordo com as seguintes categorias e apresente a categoria para o usuário.'''

n1 = int(input('Firs value: '))
n2 = int(input('Second volue: '))
n3 = int(input('Third volue: '))
sum = n1+n2+n3
if sum > 180:
    print('It will not process')
elif n1 < 90 and n2 < 90 and n3 < 90:
    print('Acute triangle')
elif n1 == 90 or n2 == 90 or n3 == 90:
    print('Right triangle')
elif n1 > 90 or n2 > 90 or n3 > 90:
    print('Obtuse triangle')