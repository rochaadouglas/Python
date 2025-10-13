class TelaPessoa:
    
    def mostra_opcoes(self):
        print("\n----- Menu Pessoa -----")
        print("1 - Cadastrar Pessoa")
        print("2 - Listar Pessoas")
        print("3 - Excluir Pessoa")
        print("0 - Retornar ao menu principal")
        
        opcao = int(input("Escolha uma opção: "))
        return opcao
     
    def pega_dados_pessoa(self):
        print("\n----- Cadastro de Pessoa -----")
        nome = input("Nome: ")
        celular = input("Celular: ")
        identificacao = input("CPF/Passaporte: ")
        return {"nome": nome, "celular": celular, "identificacao": identificacao}
    
    def mostra_pessoa(self, dados_pessoa):
        print("Nome: ", dados_pessoa["nome"])
        print("Celular: ", dados_pessoa["celular"])
        print("CPF/Passaporte: ", dados_pessoa["identificacao"])
    
    def mostra_mensagem(self, msg: str):
        print(msg)
        
    def pega_identificacao(self):
        cpf = input("CPF da pessoa que deseja selecionar: ")
        return cpf