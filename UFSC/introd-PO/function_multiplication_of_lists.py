#Recebe duas listas e retorna uma nova lista contendo a multiplicação dos elementos com o mesmo índice das listas de entrada. Caso o tamanho das listas seja diferente, inclua diretamente os elementos restantes da maior lista.
def multiplication(list1, list2):
    size = len(list1)
    ind = 0
    new_list = []
    while ind < size:
        element1 = list1[ind]
        element2 = list2[ind]
        if len(list2) < len(list1):
            list2.append(list1[ind])
        mult = element1 * element2
        new_list.append(mult)
        ind += 1
    return new_list

list1 = [12, 2, 3, 4]
list2 = [4, 5]
test = multiplication(list1, list2)
print(test)