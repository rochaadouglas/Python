# Recebe uma lista com números e retorna uma nova lista com o módulo de cada elemento da lista original.

# Receive a numeric list and return a new list with the modulus of each element in the original list.
def number_module(list):
    size = len(list)
    ind = 0
    new_list = []
    while ind < size:
        element = list[ind]
        if element < 0:
            element = element * -1
        new_list.append(element)
        ind += 1
    return new_list

list = [21, 43, -12, -9]
test = number_module(list)
print(test)