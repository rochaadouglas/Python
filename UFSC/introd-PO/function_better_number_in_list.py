# Recebe uma lista de números e retorna qual o maior número presente na lista.

# Receive a list of numbers and return what a bigger number on the list.
def bigger_number(list):
    size = len(list)
    ind = 0
    bigger = list[ind]
    while ind < size:
        actual_num = list[ind]
        if actual_num > bigger:
            bigger = actual_num
        ind += 1
    return bigger

list = [23, 2, 10, 5, 1, 0, 34]
test = bigger_number(list)
print(test)