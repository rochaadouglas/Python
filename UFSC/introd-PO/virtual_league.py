print('------------------------ VIRTUALZAO ------------------------')

my_list = [['Rickson =', 13], ['Douglas =', 18], ['Kauã =', 13], ['Jean Cabral =', 13], ['João Gui =', 30], ['Pedro Victor =', 30], ['Mateus =', 8], ['Nicolas =', 19]]

# Ordenar a lista pelo segundo elemento de cada sublista em ordem decrescente
sorted_list = sorted(my_list, key=lambda x: x[1], reverse=True)

# Exibir a matriz ordenada na vertical
for row in sorted_list:
    print(row[0], row[1])