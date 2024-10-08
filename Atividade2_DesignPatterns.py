#encoding: latin-1
from SistemaCompra import sistemaCompra
from EstrategiaDeslocamento import estrategiaDeslocamento
from CalcularImposto import calcularImposto
from Game import starGame

def main():
    
    print("Escolha uma fun��o:")
    print("1. Estr�tegia de Deslocamento")
    print("2. Sistema de Desconto em Compra")
    print("3. Calculadora de Imposto")
    print("4. Iniciar Game")
    
    escolha = input("Digite o n�mero correspondente: ")
    
    if escolha == '1':
        estrategiaDeslocamento()
    elif escolha == '2':
        sistemaCompra()
    elif escolha == '3':
        calcularImposto()
    elif escolha == '4':
        starGame()
    else:
        print("Escolha inv�lida")
        return

if __name__ == "__main__":
    main()

