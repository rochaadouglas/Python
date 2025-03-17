lista = [5, 1, 2, 5, 9]
nova_lis = []
while lista:
    menor = min(lista)
    lista.remove(menor)
    nova_lis.append(menor)
print(nova_lis)


#menor = lista.pop(0)
#menorList = min(lista)