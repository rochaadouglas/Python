#Verifique se um número está dentro de um intervalo, portanto, a função recebe três parâmetros: o início do intervalo, o fim do intervalo e o número a ser testado. Retorna verdadeiro caso pertença ao intervalo e falso caso contrário.

#Check if a number is into to interval, therefore, the function receives three parameters: beginner of the interval, the bottom of the interval and the number to be tested. Return true or false.
def interval(number, begginer=0, bottom=10):
    inter = number >= begginer and number <= bottom
    return inter

#test = interval(0, 10, 11)
#print(test)