class TelaCategoria:
    
    def tela_opcoes(self):
        print("\n------- CATEGORIA -------")
        print("1 - Incluir Categoria")
        print("2 - Alterar Categoria")
        print("3 - Listar Categoria")
        print("4 - Excluir Categoria")
        print("0 - Retornar")
        
        opcao = int(input("Escolha uma opção: "))
        return opcao
    
    def pega_dados_categoria(self):
        print("\n------- DADOS CATEGORIA -------")
        nome = input("Nome: ")
        return {"nome": nome}
    
    def seleciona_categoria(self):
        categoria = input("Categoria a ser selecionada: ")
        return categoria
    
    def mostra_mensagem(self, msg):
        print(msg)