#Elabore uma classe para representar uma Conta Bancária a qual permite saques, depósitos, verificação de saldo, informação se o saldo está no negativo e troca de senha do dono da conta. Atenção ao contexto do problema, não podemos realizar saques de valores negativos e nem de valores superiores ao saldo. Depósitos também não podem ser negativos e nem ser de R$ 0,00. Teste o funcionamento da classe executando seus métodos em, no mínimo, dois objetos distintos.

class bank_account():
    def __init__(self, opering_bal=10):
        self.balance = opering_bal
        
    def show_bank_balance(self):
        self.balance = self.balance
        print(f'{self.balance}')

obj1 = bank_account()
print(obj1.balance)