# Utilizando o dicionário capitais, crie uma função que receba um nome de Estado e retorna a respectiva capital. Caso o Estado não esteja disponível, a função retorna o texto ‘indisponível’. Implemente duas versões da função: a)utilizando apenas o operador in e o acesso padrão de elementos em um dicionário (conforme visto em aula). b)utilizando o método get

def capital_function(name, capitals):
    cap = name
    if cap in capitals:
        return capitals[cap]
    else:
        return 'Indisponível'
    
n1 = 'Pará'
capitais = {'Acre': 'Rio Branco', 'Alagoas': 'Maceió', 'Amapá': 'Macapá', 'Amazonas': 'Manaus', 'Bahia': 'Salvador', 'Ceará': 'Fortaleza', 'Distrito Federal': 'Brasília', 'Espírito Santo': 'Vitória', 'Goiás': 'Goiânia', 'Maranhão': 'São Luís', 'Mato Grosso': 'Cuiabá', 'Mato Grosso do Sul': 'Campo Grande', 'Minas Gerais': 'Belo Horizonte', 'Pará': 'Belém', 'Paraíba': 'João Pessoa', 'Paraná': 'Curitiba', 'Pernambuco': 'Recife', 'Piauí': 'Teresina', 'Rio de Janeiro': 'Rio de Janeiro', 'Rio Grande do Norte': 'Natal', 'Rio Grande do Sul': 'Porto Alegre', 'Rondônia': 'Porto Velho', 'Roraima': 'Boa Vista', 'Santa Catarina': 'Florianópolis', 'São Paulo': 'São Paulo', 'Sergipe': 'Aracaju', 'Tocantins': 'Palmas'}
test = capital_function(n1, capitais)
print(test)