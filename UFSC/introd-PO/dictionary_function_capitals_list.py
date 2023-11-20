# Utilizando os dicionários regioes, siglas e capitais, crie uma função que receba o nome de uma região e retorna uma lista com as capitais dos Estados pertencentes à região informada como parâmetro. Caso a região não exista, sua função retorna None.

regioes = {'Norte': ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'], 'Nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'], 'Centro-Oeste': ['DF', 'GO', 'MT', 'MS'], 'Sudeste': ['ES', 'MG', 'RJ', 'SP'], 'Sul': ['PR', 'RS', 'SC']}

siglas = {'AC': 'Acre', 'AL': 'Alagoas', 'AP': 'Amapá', 'AM': 'Amazonas', 'BA': 'Bahia', 'CE': 'Ceará', 'DF': 'Distrito Federal', 'ES': 'Espírito Santo', 'GO': 'Goiás', 'MA': 'Maranhão', 'MT': 'Mato Grosso', 'MS': 'Mato Grosso do Sul', 'MG': 'Minas Gerais', 'PA': 'Pará', 'PB': 'Paraíba', 'PR': 'Paraná', 'PE': 'Pernambuco', 'PI': 'Piauí', 'RJ': 'Rio de Janeiro', 'RN': 'Rio Grande do Norte', 'RS': 'Rio Grande do Sul', 'RO': 'Rondônia', 'RR': 'Roraima', 'SC': 'Santa Catarina', 'SP': 'São Paulo', 'SE': 'Sergipe', 'TO': 'Tocantins'}

capitais = {'Acre': 'Rio Branco', 'Alagoas': 'Maceió', 'Amapá': 'Macapá', 'Amazonas': 'Manaus', 'Bahia': 'Salvador', 'Ceará': 'Fortaleza', 'Distrito Federal': 'Brasília', 'Espírito Santo': 'Vitória', 'Goiás': 'Goiânia', 'Maranhão': 'São Luís', 'Mato Grosso': 'Cuiabá', 'Mato Grosso do Sul': 'Campo Grande', 'Minas Gerais': 'Belo Horizonte', 'Pará': 'Belém', 'Paraíba': 'João Pessoa', 'Paraná': 'Curitiba', 'Pernambuco': 'Recife', 'Piauí': 'Teresina', 'Rio de Janeiro': 'Rio de Janeiro', 'Rio Grande do Norte': 'Natal', 'Rio Grande do Sul': 'Porto Alegre', 'Rondônia': 'Porto Velho', 'Roraima': 'Boa Vista', 'Santa Catarina': 'Florianópolis', 'São Paulo': 'São Paulo', 'Sergipe': 'Aracaju', 'Tocantins': 'Palmas'}

def capitalsList(dicio, regiao):
    regioes = dicio.get(regiao)
    l = []
    ca = []
    for i in regioes:
        l.append(siglas.get(i))
        for c in l:
            ca.append(capitais.get(c))
    return list(set(ca))

print(capitalsList(regioes, 'Sul'))