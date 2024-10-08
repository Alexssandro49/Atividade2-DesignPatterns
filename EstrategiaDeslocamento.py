#encoding: latin-1
from abc import ABC, abstractmethod

# Interface Strategy
class TravelStrategy(ABC):
    @abstractmethod
    def travel_time(self, distancia: float) -> float:
        pass

# Estrat�gia para Carro
class CarStrategy(TravelStrategy):
    def travel_time(self, distancia: float) -> float:
        velocidade = 60 
        return distancia / velocidade

# Estrat�gia para Bicicleta
class BicycleStrategy(TravelStrategy):
    def travel_time(self, distancia: float) -> float:
        velocidade = 15 
        return distancia / velocidade

# Estrat�gia para Caminhada
class WalkStrategy(TravelStrategy):
    def travel_time(self, distancia: float) -> float:
        velocidade = 5 
        return distancia / velocidade

# Contexto de Viagem
class TravelContext:
    def __init__(self, strategy: TravelStrategy = None):
        self._strategy = strategy
    
    def set_strategy(self, strategy: TravelStrategy):
        self._strategy = strategy
    
    def calculate_time(self, distancia: float) -> float:
        if not self._strategy:
            raise ValueError("Nenhuma estrat�gia de viagem definida")
        return self._strategy.travel_time(distancia)

# Interface simples para o usu�rio
def estrategiaDeslocamento():
    context = TravelContext()
    
    print("Escolha o meio de transporte:")
    print("1. Carro")
    print("2. Bicicleta")
    print("3. A p�")
    
    escolha = input("Digite o n�mero correspondente: ")
    
    if escolha == '1':
        context.set_strategy(CarStrategy())
    elif escolha == '2':
        context.set_strategy(BicycleStrategy())
    elif escolha == '3':
        context.set_strategy(WalkStrategy())
    else:
        print("Escolha inv�lida")
        return
    
    distancia = float(input("Digite a dist�ncia a ser percorrida (em km): "))
    
    tempo = context.calculate_time(distancia)
    print(f"Tempo estimado de viagem: {tempo:.2f} horas")
