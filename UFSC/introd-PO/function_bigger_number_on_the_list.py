#Recebe uma lista com números, encontra o maior número dessa lista e retorna uma nova lista com todos os números da lista original divididos pelo maior número.
def bigger_number(list):
    size = len(list)
    ind = 0
    new_list = []
    while ind < size:
        element = list[ind]
        bigger = max(list)
        division = element / bigger
        new_list.append(division)
        ind += 1
    return new_list

list = [12, 10, 3, 30]
test = bigger_number(list)
print(test)