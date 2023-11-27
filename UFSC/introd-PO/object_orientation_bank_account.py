#Elabore uma classe para representar uma Conta Bancária a qual permite saques, depósitos, verificação de saldo, informação se o saldo está no negativo e troca de senha do dono da conta. Atenção ao contexto do problema, não podemos realizar saques de valores negativos e nem de valores superiores ao saldo. Depósitos também não podem ser negativos e nem ser de R$ 0,00. Teste o funcionamento da classe executando seus métodos em, no mínimo, dois objetos distintos.

class bank_account():
    def __init__(self, opering_bal=0, password='douglas'):
        self.balance = opering_bal
        self.__password = password
        
    def show_bank_balance(self):
        self.balance = self.balance

    def cash_deposit(self, amount_money):
        self.amount_money = amount_money
        if self.amount_money > 0:
            self.balance = self.balance + amount_money

    def withdraw_money(self, withdraw_value):
        self.withdraw_value = withdraw_value
        if self.balance > 0:
            if withdraw_value <= self.balance:   
                self.balance = self.balance - withdraw_value
            
    def change_password(self, new_password):
        self.__password = new_password 

obj1 = bank_account()
print(obj1.balance)
obj1.cash_deposit(2)
print(obj1.balance)
obj1.withdraw_money(2)
print(obj1.balance)
obj1.change_password('dodo')
#print(obj1.password)