# Recebe uma lista com conteúdos de diferentes tipos e mostra-os para o usuário em ordem inversa (essa função não tem retorno).

# Receive a list with different types elements and show it to user in inversion order. This function has no return.
def inverted_list(list):
    size = len(list)
    ind = size - 1
    while ind >= 0:
        print(f'{list[ind]}')
        ind -= 1

list = ['=', 3, 'olá', -1, 'hello']
test = inverted_list(list)