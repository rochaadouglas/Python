class TelaAtor():
    
    def tela_opcoes(self):
        print("\n-------ATOR -------")
        print("1 - Incluir Ator")
        print("2 - Alterar Ator")
        print("3 - Listar Ator")
        print("4 - Excluir Ator")
        print("0 - Retornar")
        
        opcao = int(input("Escolha uma opção: "))
        return opcao
    
    def pega_dados_ator(self):
        print("\n------- DADOS ATOR -------")
        id = input("Id: ")
        nome = input("Nome: ")
        data_de_nascimento = input("Data de nascimento: ")
        nacionalidade = input("Nacionalidade: ")
        return {"id": id, "nome": nome, "data_de_nascimento": data_de_nascimento, 
                "nacionalidade": nacionalidade}
        
    def mostra_ator(self, dados_ator):
        print("\n------- LISTA DE ATORES -------")
        print("ID DO ATOR:", dados_ator["id"])
        print("NOME DO ATOR:", dados_ator["nome"])
        print("DATA DE NASCIMENTO DO ATOR:", dados_ator["data_de_nascimento"])
        print("NACIONALIDADE DO ATOR:", dados_ator["nacionalidade"])
        
    def seleciona_ator(self):
        ator = input("\nId do ator a ser selecionado: ")
        return ator
    
    def mostra_mensagem(self, msg):
        print(msg)