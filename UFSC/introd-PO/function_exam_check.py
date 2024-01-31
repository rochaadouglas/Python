# Dado um gabarito de uma prova com 10 questões cujas respostas podem ser A, B, C, D ou E, elabore uma função que receba uma prova por parâmetro e retorna a quantidade de acertos. Gabarito: A,A,C,E,D,B,C,E,B,D.

# In a test answer sheet with 10 questions when the answers can be A, B, C, D or E, make a function that receive a test by parameter and return the amount hits. Test answer sheet: A,A,C,E,D,B,C,E,B,D
def exam_check(exam, gabarito=['A', 'A', 'C', 'E', 'D', 'B', 'C', 'E', 'B', 'D']):
    size = len(gabarito)
    element = exam
    ind = 0
    ind_exam = 0
    sum = 0
    while ind < size:
        element_gab = gabarito[ind]
        element_exam = element[ind_exam]
        if element_gab == element_exam:
            sum = sum + 1
        ind += 1
        ind_exam += 1
    return sum

exam = ['B', 'A', 'D', 'E', 'D', 'C', 'B', 'D', 'B', 'D']
test = exam_check(exam)
print(test)