# Recebe um número inteiro representando a quantidade de números aleatórios  desejados e retorna uma lista com essa quantidade de números inteiros produzidos aleatoriamente. Utilize alguma função do módulo random.

# Receive an integer number representing the amount of random numbers and return a list with that amount of integer numbers. Use some function from random module.
from random import randint 
def random_number(number):
    ind = 0
    size = number
    new_list = []
    while ind < size:
        num = randint(0, 100)
        new_list.append(num)
        ind += 1
    return new_list

test = random_number(6)
print(test)