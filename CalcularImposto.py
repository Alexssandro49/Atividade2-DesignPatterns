#encoding: latin-1
from abc import ABC, abstractmethod

class ImpostoStrategy(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass

class ImpostoRenda(ImpostoStrategy):
    def calcular(self, valor: float) -> float:
        taxa = 0.21  # 21% de imposto sobre a renda
        return valor * taxa

class ImpostoVendas(ImpostoStrategy):
    def calcular(self, valor: float) -> float:
        taxa = 0.13  # 13% de imposto sobre vendas
        return valor * taxa

class ImpostoProduto(ImpostoStrategy):
    def calcular(self, valor: float) -> float:
        taxa = 0.03  # 3% de imposto sobre produtos
        return valor * taxa

#Calcular Imposto
class CalculadoraDeImposto:
    def __init__(self, strategy: ImpostoStrategy = None):
        self._strategy = strategy

    def set_imposto_strategy(self, strategy: ImpostoStrategy):
        self._strategy = strategy

    def calcular_imposto(self, valor: float) -> float:
        if not self._strategy:
            raise ValueError("Nenhuma estratégia de imposto definida")
        return self._strategy.calcular(valor)

def calcularImposto():
    valor = float(input("Digite o valor sobre o qual calcular o imposto: R$ "))
    
    calculadora = CalculadoraDeImposto()
    
    print("Escolha o tipo de imposto:")
    print("1. Imposto sobre a Renda (21%)")
    print("2. Imposto sobre Vendas (13%)")
    print("3. Imposto sobre Produtos (3%)")
    
    choice = input("Digite o número correspondente: ")
    
    if choice == '1':
        calculadora.set_imposto_strategy(ImpostoRenda())
    elif choice == '2':
        calculadora.set_imposto_strategy(ImpostoVendas())
    elif choice == '3':
        calculadora.set_imposto_strategy(ImpostoProduto())
    else:
        print("Escolha inválida")
        return
    
    imposto = calculadora.calcular_imposto(valor)
    print(f"Imposto a ser pago: R$ {imposto:.2f}")

