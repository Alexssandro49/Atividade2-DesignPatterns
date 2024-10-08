#encoding: latin-1
from abc import ABC, abstractmethod

# Interface Strategy
class TravelStrategy(ABC):
    @abstractmethod
    def travel_time(self, distancia: float) -> float:
        pass

# Estratégia para Carro
class CarStrategy(TravelStrategy):
    def travel_time(self, distancia: float) -> float:
        velocidade = 60 
        return distancia / velocidade

# Estratégia para Bicicleta
class BicycleStrategy(TravelStrategy):
    def travel_time(self, distancia: float) -> float:
        velocidade = 15 
        return distancia / velocidade

# Estratégia para Caminhada
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
            raise ValueError("Nenhuma estratégia de viagem definida")
        return self._strategy.travel_time(distancia)

# Interface simples para o usuário
def estrategiaDeslocamento():
    context = TravelContext()
    
    print("Escolha o meio de transporte:")
    print("1. Carro")
    print("2. Bicicleta")
    print("3. A pé")
    
    escolha = input("Digite o número correspondente: ")
    
    if escolha == '1':
        context.set_strategy(CarStrategy())
    elif escolha == '2':
        context.set_strategy(BicycleStrategy())
    elif escolha == '3':
        context.set_strategy(WalkStrategy())
    else:
        print("Escolha inválida")
        return
    
    distancia = float(input("Digite a distância a ser percorrida (em km): "))
    
    tempo = context.calculate_time(distancia)
    print(f"Tempo estimado de viagem: {tempo:.2f} horas")
