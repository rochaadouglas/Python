#Recebe uma lista com números e retorna um nova lista contendo os números primos presentes nessa lista.

# Receive a list numbers and return a new list containing the prime numbers present on the list.
from function_cousin import cousin_number
def cousin_list(list):
    size = len(list)
    ind = 0
    new_list = []
    while ind < size:
        element = list[ind]
        cousin = cousin_number(element)
        if cousin == True:
            new_list.append(element)
        ind += 1
    return new_list

list = [11, 3, 4, 8, 13]
test = cousin_list(list)
print(test)