#Recebe uma matriz contendo textos e informe para o usuário quais linhas e colunas possuem valores nulos (‘’).

def nullValue(matrix):
    size = len(matrix)
    line = 0
    while line < size:
        amount_col = len(matrix[line])
        col = 0
        while col < amount_col:
            element = matrix[line][col]
            if element == '':
                print(f'line {line}, column {col} no value')
            col += 1
        line += 1

m = [['dodo', 'ndjend', 'faca'], ['', 'diga', 'valor'], ['', 'dehu', 'kaka']]
test = nullValue(m)