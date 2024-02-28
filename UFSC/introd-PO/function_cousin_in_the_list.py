# Recebe uma lista de números e retorna quantos números primos a lista possui. Importe sua função para verificação de primos diretamente do módulo em que ela se encontra (arquivo .py) e utilize-a para resolver esse exercício.

# Receive a list of numbers and returns how many prime numbers are in the list. Import your function to check prime numbers in the module that are it.
from function_cousin import cousin_number
def cousin_list(list):
    size = len(list)
    ind = 0
    cousin = 0
    while ind < size:
        value = cousin_number(list[ind])
        if value == True:
            cousin = cousin + 1
        ind += 1
    return cousin

#list = [2, 3, 8, 11, 12, 15, 31]
#test = cousin_list(list)
#print(test)