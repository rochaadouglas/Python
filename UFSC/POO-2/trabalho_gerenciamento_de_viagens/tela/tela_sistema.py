class TelaSistema:
    
    def tela_opcoes(self):
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Gerenciar Pessoas")
        print("0 - Sair do sistema")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida! Digite apenas números.")
    
    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")