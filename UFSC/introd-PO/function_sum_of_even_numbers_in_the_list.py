# Recebe uma lista de números e retorna o somatório dos números pares presentes na lista.

# Receive a number list and return the sum of even numbers on list.
def even_number(list):
    size = len(list)
    ind = 0
    sum = 0
    while ind < size:
        value = list[ind]
        if value % 2 == 0:
            sum = sum + value
        ind += 1
    return sum

list = [2, 5, 7, 8, 12]
test = even_number(list)
print(test)