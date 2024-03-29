# Elabore uma classe para representar um Carro Simplificado. Esta classe deve armazenar as informações referentes à capacidade (em litros) do tanque de combustível do carro, a quantidade de gasolina atual e o consumo médio de combustível (em km/litro). Nesta classe, implemente os seguintes métodos:
# a)abastece: recebe uma quantidade de gasolina e adiciona essa quantidade no tanque. Atenção à capacidade do tanque e à quantidade atual de combustível. O método retorna True ou False, dependendo se foi possível realizar o abastecimento.
# b)informaGasolina: esse método retorna a quantidade gasolina disponível no tanque.
# c)consomeGasolina: recebe uma distância, em km, e, utilizando o consumo médio do carro, consome a respectiva quantidade de gasolina do tanque do carro. Atenção pois o tanque de combustível não pode conter uma quantidade negativa de gasolina.
# d)estáNoReserva: retorna um valor lógico indicando se a quantidade de gasolina atual está abaixo de 10% da capacidade total do tanque.

# Elaborate a class to represent a Simplified Car. This class must store the information referents to capacity of car fuel tank, the actual fuel amount and fuel average consume. In this class make the methods:
# a)to fuel: receive a fuel amount and add that amount on the fuel tank. Attention to tank capacity and to fuel actual amount. The method returns True or False if was possible to realize the car fueling.
# b)inform fuel: This method returns the fuel available amount on tank.
# c)fuel consume: receive a distance in Km and using the car average consume it consume the respective amount of fuel of the car tank.The fuel tank can't have a negative amount.
# d)fuel reserve: return a logical value indicating whether the actual amount of fuel are below 10% from tank total capacity.
class Car():
    def __init__(self, capacity=70, current_liter=5):
        self.capacity = capacity
        self.current_liter = current_liter
        self.avarege_cons = capacity

    def to_fuel(self, fuel):
        self.fuel = fuel
        if (self.fuel + self.current_liter) <= self.capacity:
            self.current_liter = self.current_liter + self.fuel
            return True
        else:
            return False
    
    def show_gasoline(self):
        self.new_liter = self.current_liter

    def gasoline_cunsume(self, km):
        self.consume = km / self.avarege_cons
        self.new_liter = self.new_liter - self.consume

    def low_gasoline(self):
        self.new_liter = self.new_liter

car1 = Car()
print(f'{car1.to_fuel(65)}')
car1.show_gasoline()
print(car1.current_liter)
car1.gasoline_cunsume(600)
print(f'{car1.consume:.2} Km/l')
print(f'{car1.new_liter}')
