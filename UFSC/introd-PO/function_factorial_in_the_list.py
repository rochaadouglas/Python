# Recebe uma lista de números e apresenta para o usuário o fatorial de cada um deles (utilize a função factorial do módulo math).

# Receive a list numbers and show it to user the factorial of each them.
from math import factorial
def factorial_list(list):
    size = len(list)
    ind = 0
    while ind < size:
        value = list[ind]
        fact = factorial(value)
        print(fact)
        ind += 1

list = [4, 5, 2, 3]
test = factorial_list(list)