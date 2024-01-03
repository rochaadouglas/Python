#Obtenha via entrada do usuário dois números inteiros positivos quaisquer (início e fim) e exiba as tabuadas dos números presentes no intervalo entre início e fim (incluindo esses números).

#Get with user input two any positive whole numbers (beginning and end) and show the multiplication tables between beginning and end.
num1 = int(input('Beginning value: '))
num2 = int(input('End value: '))
count = num1
while count <= num2:
    count_tab = 1
    while count_tab <= 10:
        mult = count * count_tab
        print(f'{count}x{count_tab} = {mult}')
        count_tab += 1
    count += 1
    print()