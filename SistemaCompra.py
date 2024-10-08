#encoding: latin-1
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass

class LoyaltyDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        desconto = 0.05  # 5% de desconto
        return total * (1 - desconto)

class SeasonalDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        desconto = 0.10  # 10% de desconto
        return total * (1 - desconto)

class BulkPurchaseDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        desconto = 0.15  # 15% de desconto
        return total * (1 - desconto)

class ShoppingCart:
    def __init__(self, total: float):
        self.total = total
        self._discount_strategy = None

    def set_discount_strategy(self, strategy: DiscountStrategy):
        self._discount_strategy = strategy

    # Calcular o pre�o final com o desconto aplicado
    def get_final_price(self) -> float:
        if not self._discount_strategy:
            raise ValueError("Nenhuma estrat�gia de desconto definida")
        return self._discount_strategy.apply_discount(self.total)

def sistemaCompra():
    total = float(input("Digite o valor total da compra: R$ "))
    
    carrinho = ShoppingCart(total)
    
    print("Escolha o tipo de desconto:")
    print("1. Desconto por Fidelidade (5%)")
    print("2. Desconto Sazonal (10%)")
    print("3. Desconto por Volume de Compra (15%)")
    
    choice = input("Digite o n�mero correspondente: ")
    
    if choice == '1':
        carrinho.set_discount_strategy(LoyaltyDiscount())
    elif choice == '2':
        carrinho.set_discount_strategy(SeasonalDiscount())
    elif choice == '3':
        carrinho.set_discount_strategy(BulkPurchaseDiscount())
    else:
        print("Escolha inv�lida")
        return
    
    final_price = carrinho.get_final_price()
    print(f"Valor total com desconto: R$ {final_price:.2f}")

