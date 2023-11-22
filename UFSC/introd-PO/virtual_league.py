print('------------------------ VIRTUALZAO ------------------------')

my_list = [['Rickson =', 14], ['Douglas =', 21], ['Kauã =', 14], ['Jean Cabral =', 13], ['João Gui =', 30], ['Pedro Victor =', 33], ['Mateus =', 9], ['Nicolas =', 20]]

# Ordenar a lista pelo segundo elemento de cada sublista em ordem decrescente
sorted_list = sorted(my_list, key=lambda x: x[1], reverse=True)

# Exibir a matriz ordenada na vertical
for row in sorted_list:
    print(row[0], row[1])