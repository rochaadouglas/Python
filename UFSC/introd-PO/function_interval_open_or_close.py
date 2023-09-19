#Crie uma nova versão da função do exercício 1, porém agora com um parâmetro opcional o qual informa se o intervalo é aberto ou fechado, ou seja, se os valores de início e fim do intervalo também são considerados na verificação. (Teste a execução dessa função com e sem o parâmetro opcional).
def inter(num, begginer, bottom=5):
    if num >= begginer and num <= bottom:
        return 'intervalo fechado'
    else:
        return 'intervalo aberto'
test = inter(11, 1)
print(test)