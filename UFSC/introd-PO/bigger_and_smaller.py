#Obtenha três valores numéricos e, ao final, apresente o maior e o menor valor em uma única mensagem. Considere que os valores são sempre diferentes entre si. 

#Get three numeric values and at the end it shows the smallest and largest in a single message. You can consider that the values are always different from each other.
n1 = int(input('First value: '))
n2 = int(input('Second value: '))
n3 = int(input('Third value: '))
if n1 > n2 and n2 > n3:
    print(f'{n1}, {n3}')
elif n2 > n1 and n1 > n3: 
    print(f'The bigger volue is {n2}, the smaller value is {n3}')
elif n3 > n2 and n2 > n1:
    print(f'The bigger volue is {n3}, the smaller value is {n1}')
elif n1 > n3 and n3 > n2:
    print(f'The bigger volue is {n1}, the smaller value is {n2}')