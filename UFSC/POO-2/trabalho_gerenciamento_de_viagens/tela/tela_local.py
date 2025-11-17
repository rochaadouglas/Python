import FreeSimpleGUI as sg


class TelaLocal:
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
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao
        
    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeak4')
        layout = [
            [sg.Text('----- Gerenciamento de Locais -----', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção:', font=("Helvica", 15))]
        ]
        self.window = sg.Window('Sistema de Gerenciamento de Viagens').Layout(layout)
        
    def close(self):
        self.__window.Close()
    
    def open(self):
        button, values = self.__window.Read()
        return button, values