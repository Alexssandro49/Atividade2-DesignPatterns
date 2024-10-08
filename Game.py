#encoding: latin-1
from abc import ABC, abstractmethod

class EstrategiaDeAtaque(ABC):
    @abstractmethod
    def atacar(self) -> None:
        pass

class AtaqueCorpoACorpo(EstrategiaDeAtaque):
    def atacar(self) -> None:
        print("Ataque corpo a corpo: O personagem desferiu um soco poderoso!")

class AtaqueDistancia(EstrategiaDeAtaque):
    def atacar(self) -> None:
        print("Ataque � dist�ncia: O personagem lan�ou uma flecha certeira!")

class AtaqueMagico(EstrategiaDeAtaque):
    def atacar(self) -> None:
        print("Ataque m�gico: O personagem lan�ou uma bola de fogo!")

class Personagem:
    def __init__(self, nome: str, estrategia: EstrategiaDeAtaque = None):
        self.nome = nome
        self._estrategia = estrategia

    def set_estrategia(self, estrategia: EstrategiaDeAtaque) -> None:
        self._estrategia = estrategia

    def atacar(self) -> None:
        if not self._estrategia:
            raise ValueError(f"{self.nome} n�o tem uma estrat�gia de ataque definida")
        print(f"{self.nome} est� se preparando para atacar...")
        self._estrategia.atacar()

def escolher_estrategia() -> EstrategiaDeAtaque:
    print("\nEscolha a estrat�gia de ataque:")
    print("1. Ataque corpo a corpo")
    print("2. Ataque � dist�ncia")
    print("3. Ataque m�gico")
    
    escolha = input("Digite o n�mero correspondente: ")
    
    if escolha == '1':
        return AtaqueCorpoACorpo()
    elif escolha == '2':
        return AtaqueDistancia()
    elif escolha == '3':
        return AtaqueMagico()
    else:
        print("Escolha inv�lida, tente novamente.")
        return escolher_estrategia()

# Fun��o principal para o usu�rio criar personagens e simular ataques
def starGame():
    nome_personagem = input("Digite o nome do personagem: ")
    personagem = Personagem(nome_personagem)
    
    while True:
        estrategia = escolher_estrategia()
        personagem.set_estrategia(estrategia)
        
        personagem.atacar()
        
        continuar = input("\nDeseja alterar a estrat�gia de ataque? (s/n): ")
        if continuar.lower() != 's':
            break

