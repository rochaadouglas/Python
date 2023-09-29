#Recebe uma lista de números e um número qualquer e retorna um valor lógico indicando se o número está presente na lista.
def in_the_list(list, number):
    size = len(list)
    ind = 0
    num = number
    while ind < size:
        value = list[ind]
        if value == num:
            return True
        ind += 1
    else:
        return False

#list = [21, 9, 8, 33]
test = in_the_list([21, 9, 8, 33], 22)
print(test)