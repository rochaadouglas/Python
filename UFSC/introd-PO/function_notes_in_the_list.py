#Recebe uma lista com notas (valores em ponto flutuante) entre 0 e 10 e retorna uma lista contendo a média e a moda das notas. Para o cálculo da média e mediana, utilize funções do módulo statistics. Caso a lista contenha notas inválidas, não realize o cálculo e a função não retorna nada.
from statistics import median
from statistics import mode
def note_list(list):
    size = len(list)
    ind = 0
    new_list = []
    median_mode = []
    while ind < size:
        value = list[ind]
        if value >= 0 and value <= 10:
            new_list.append(value)
        else:
            return None
        ind += 1
    median_mode.append(median(new_list))
    median_mode.append(mode(new_list))
    return median_mode

list = [3.0, 3.0, 5.0, 5.0, 10.0]
test = note_list(list)
print(test)