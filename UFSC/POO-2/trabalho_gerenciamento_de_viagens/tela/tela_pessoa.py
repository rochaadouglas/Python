import FreeSimpleGUI as sg


class TelaPessoa:
    def __init__(self):
        self.__window = None
        self.init_opcoes()
    
    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('Darkteal4')
        layout = [
            [sg.Text('----- MENU PESSOA -----', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Cadastrar Pessoa', "RD1", key='1')],
            [sg.Radio('Listar Pessoa', "RD1", key='2')],
            [sg.Radio('Excluir Pessoa', "RD1", key='3')],
            [sg.Radio('Retornar ao menu principal', "RD1", key='0')],
            [sg.Button('Confirmar', sg.Cancel('Cancelar'))]
        ]
        self.__window = sg.Window('Sistema de Gerenciamento de Viagens').Layout(layout)
        
    def pega_dados_pessoa(self):
        sg.ChangeLookAndFeel('Darkteal4')
        layout = [
            [sg.Text('----- PEGA DADOS DA PESSOA -----')],
            [sg.Text('Nome: ', size=(15, 1)), sg.InputText('','nome')],
            [sg.Text('Celular: ', size=(15, 1)), sg.InputText('', 'celular')],
            [sg.Text('CPF/Passaporte: ', size=(15, 1)), sg.InputText('', 'identificacao')]
        ]
        
        
        
        
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
    
    def close(self):
        self.__window.Close()
    
    def open(self):
        button, values = self.__window.Read()
        return button, values