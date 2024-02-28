# Recebe duas listas de números e retorna o valor lógico verdadeiro caso a primeira lista tenha um somatório maior do que o da segunda lista. Para o cálculo do somatório utilize a função sum, já inclusa no Python.

# Receive two lists numbers and return a true logic value if the first list has a bigger sum than second list. For the sum calculation use the "sum" function, already on the Python library.
def bigger_value(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    if sum1 > sum2:
        return True
    else:
        return False

list1 = [2, 3, 5, 4]
list2 = [1, 6, 0, 0]
test = bigger_value(list1, list2)
print(test)