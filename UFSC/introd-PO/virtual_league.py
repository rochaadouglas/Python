print('------------------------ VIRTUALZAO ------------------------')

def ourList(matrix):
    size = len(matrix)
    line = 0
    new_list = []
    menor = matrix[0][1]
    lin_name = 0
    while line < size:
        amount_col = len(matrix[line])
        col = 1
        while col < amount_col:
            element = matrix[line][col]
            col_name = matrix[0]
            if element >= menor:
                lin_name = matrix[line][0] 
                menor = element 
                new_list.append(lin_name)
                new_list.append(menor)
            col += 1
        line += 1
    return new_list

my_list = [['r',0], ['d',3], ['k',1], ['J',3],['c',0], ['p',0], ['m',0], ['n',0]]
test = ourList(my_list)
print(test)
