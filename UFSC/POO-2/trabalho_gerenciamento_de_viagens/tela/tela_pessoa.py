class TelaPessoa:
    
    def mostra_opcoes(self):
        print("\n----- Menu Pessoa -----")
        print("1 - Cadastrar Pessoa")
        print("2 - Listar Pessoas")
        print("3 - Excluir Pessoa")
        print("0 - Retornar ao menu principal")
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            print("Opção inválida! Digite apenas números.")
    
    
    def pega_dados_pessoa(self):
        print("\n----- Cadastro de Pessoa -----")
        nome = input("None: ")
        celular = input("Celular: ")
        identificacao = input(" CPF/Passaporte: ")
        return {"nome": nome, "celular": celular, "identificacao": identificacao}
    
    
    def mostra_pessoa(self, pessoa):
        print(f"{pessoa.nome} - {pessoa.identificacao} ({pessoa.celular})")
        
    
    def mostra_mensagem(self, msg: str):
        print(msg)
        
    
    def pega_identificacao(self):
        return input("Digite o CPF/Passaporte da pessoa: ")