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
        print("Ataque à distância: O personagem lançou uma flecha certeira!")

class AtaqueMagico(EstrategiaDeAtaque):
    def atacar(self) -> None:
        print("Ataque mágico: O personagem lançou uma bola de fogo!")

class Personagem:
    def __init__(self, nome: str, estrategia: EstrategiaDeAtaque = None):
        self.nome = nome
        self._estrategia = estrategia

    def set_estrategia(self, estrategia: EstrategiaDeAtaque) -> None:
        self._estrategia = estrategia

    def atacar(self) -> None:
        if not self._estrategia:
            raise ValueError(f"{self.nome} não tem uma estratégia de ataque definida")
        print(f"{self.nome} está se preparando para atacar...")
        self._estrategia.atacar()

def escolher_estrategia() -> EstrategiaDeAtaque:
    print("\nEscolha a estratégia de ataque:")
    print("1. Ataque corpo a corpo")
    print("2. Ataque à distância")
    print("3. Ataque mágico")
    
    escolha = input("Digite o número correspondente: ")
    
    if escolha == '1':
        return AtaqueCorpoACorpo()
    elif escolha == '2':
        return AtaqueDistancia()
    elif escolha == '3':
        return AtaqueMagico()
    else:
        print("Escolha inválida, tente novamente.")
        return escolher_estrategia()

# Função principal para o usuário criar personagens e simular ataques
def starGame():
    nome_personagem = input("Digite o nome do personagem: ")
    personagem = Personagem(nome_personagem)
    
    while True:
        estrategia = escolher_estrategia()
        personagem.set_estrategia(estrategia)
        
        personagem.atacar()
        
        continuar = input("\nDeseja alterar a estratégia de ataque? (s/n): ")
        if continuar.lower() != 's':
            break

