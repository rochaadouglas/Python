#Um texto em Python pode ser acessado via índices da mesma forma que uma lista. Exemplo: palavra = ‘abacaxi’ → palavra[0]: ‘a’, palavra[1]: ‘b’. Assim como numa lista, é possível utilizar a função len para obter o tamanho de um texto. Exemplo: len(palavra) → 7. Elabore uma função que receba um texto como parâmetro e retorna um valor lógico indicando se o texto é palíndromo. Um palíndromo é uma frase ou palavra que mantém o mesmo sentido quando lida de trás pra frente. Exemplos: reger, rir, radar, ele, esse, ama, aia, etc. 
def palindrome(text):
    size = len(text)
    ind = size - 1
    while ind >= 0:
        ind_inicial = 0
        element = text[ind]
        element_inicial = text[ind_inicial]
        if element == element_inicial:
            return True
        ind_inicial += 1
        ind -= 1
    else:
        return False

text = 'eede'
test = palindrome(text)
print(test)