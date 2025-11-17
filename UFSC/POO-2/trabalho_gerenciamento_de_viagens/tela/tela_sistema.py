import FreeSimpleGUI as sg


class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()
        
    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao
    
    def close(self):
        self.__window.Close()
    
    def init_components(self):
        sg.ChangeLookAndFeel("DarkTeal4")
        layout = [
            [sg.Text('Sistema de Gerenciamento de Viagens', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Gerenciar Pessoas', "RD1", key='1')],
            [sg.Radio('Gerenciar Local', "RD1", key='2')],
            [sg.Radio('Finalizar Sistema', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Viagens').layout(layout)