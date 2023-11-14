print('------------------------ VIRTUALZAO ------------------------')

my_list = [['Rickson =', 0], ['Douglas =', 12], ['Kauã =', 6], ['Jean Cabral =', 7], ['João Gui =', 18], ['Pedro Victor =', 15], ['Mateus =', 5], ['Nicolas =', 13]]

# Ordenar a lista pelo segundo elemento de cada sublista em ordem decrescente
sorted_list = sorted(my_list, key=lambda x: x[1], reverse=True)

# Exibir a matriz ordenada na vertical
for row in sorted_list:
    print(row[0], row[1])