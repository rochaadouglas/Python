#Mostre todos os números ímpares no intervalo de 0 ao número informado pelo usuário. Mostre os ímpares apenas se a entrada for maior do que 1.

#Showing all of odd numbers between 0 and reported number the user. Just show it if the input bigger than 1.
num = int(input('Report your number: ')) 
cont = 1
if num > 1:
    while cont < num:
        print(cont)
        cont += 2