print('------------------------ VIRTUALZAO ------------------------')

def ourList(matrix):
    size = len(matrix)
    line = 0
    new_list = []
    menor = matrix[0][1]
    while line < size:
        amount_col = len(matrix[line])
        col = 1
        while col < amount_col:
            element = matrix[line][col]
            if element > menor:
                new_list.append(element)
            col += 1
        line += 1
    return new_list

my_list = [['r',0], ['d',0], ['k',1], ['J',0],['c',0], ['p',0], ['m',0], ['n',0]]
test = ourList(my_list)
print(test)
