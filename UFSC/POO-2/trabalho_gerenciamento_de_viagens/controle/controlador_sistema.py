from controle.controlador_pessoa import ControladorPessoa
from tela.tela_pessoa import TelaPessoa

class ControladorSistema:
    
    def __init__(self):
        self.__controlador_sistema = ControladorPessoa(self)
        self.__tela_pessoa = TelaPessoa()
        
        
    def abre_sistema(self):
        while True:
            print("\n===== MENU PRINCIPAL =====")
            print("1 - Gerenciar Pessoas")
            print("0 - Sair do sistema")
            try:
                opcao = int(input("Escolha uma opção: "))
            except ValueError:
                print("Opção inválida! Digite apenas números.")
                
            if opcao == 1:
                self.__tela_pessoa.mostra_opcoes()
            elif opcao == 0:
                print("Encerrando o sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")