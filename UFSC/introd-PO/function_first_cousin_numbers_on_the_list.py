#Recebe uma quantidade (N) e um número de início e retorna uma lista com os primeiros N números primos a partir do número recebido (utilize sua função para obtenção do próximo número primo).

# Receive an amount (N) and a beginning number and return a list with the first prime numbers from the received numbers.
from function_cousin import cousin_number
def first_cousin_numbers(amount, number):
    size = amount
    ind = number
    count = 1
    new_list = []
    while count <= size:
        cousin = cousin_number(ind)
        if cousin == True:
            new_list.append(ind)
        ind += 1
        count += 1
    return new_list

test = first_cousin_numbers(5, 4)
print(test)