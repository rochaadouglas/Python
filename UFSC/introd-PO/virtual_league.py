print('------------------------ VIRTUALZAO ------------------------')

my_list = [['Rickson =', 9], ['Douglas =', 15], ['Kauã =', 12], ['Jean Cabral =', 7], ['João Gui =', 21], ['Pedro Victor =', 24], ['Mateus =', 8], ['Nicolas =', 13]]

# Ordenar a lista pelo segundo elemento de cada sublista em ordem decrescente
sorted_list = sorted(my_list, key=lambda x: x[1], reverse=True)

# Exibir a matriz ordenada na vertical
for row in sorted_list:
    print(row[0], row[1])