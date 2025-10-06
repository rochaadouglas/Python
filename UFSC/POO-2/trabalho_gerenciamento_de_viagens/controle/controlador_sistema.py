from controle.controlador_pessoa import ControladorPessoa

class ControladorSistema:
    
    def __init__(self):
        self.__controlador_sistema = ControladorPessoa()
        
        
    def abre_sistema(self):
        while True:
            print("\n===== MENU PRINCIPAL =====")
            print("1 - Gerenciar Pessoas")
            print("0 - Sair do sistema")
            try:
                opcao = int(input("Escolha uma opção: "))
                return opcao
            except ValueError:
                print("Opção inválida! Digite apenas números.")
                
            if opcao == 1:
                self.__controlador_pessoa.abre_tela()
            elif opcao == 0:
                print("Encerrando o sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")