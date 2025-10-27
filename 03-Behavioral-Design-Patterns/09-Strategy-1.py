# Strategy Interface
class DiscountStrategy:
    def apply_discount(self, amount):
        pass

# Concrete Strategies
class ChristmasDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.8  # 20% تخفیف

class BlackFridayDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.5  # 50% تخفیف

class NoDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount  # بدون تخفیف

# Context
class ShoppingCart:
    def __init__(self, discount_strategy):
        self.discount_strategy = discount_strategy

    def calculate_total(self, amount):
        return self.discount_strategy.apply_discount(amount)

# استفاده از استراتژی‌های مختلف
cart = ShoppingCart(ChristmasDiscount())
print(cart.calculate_total(100))  # خروجی: 80.0

cart = ShoppingCart(BlackFridayDiscount())
print(cart.calculate_total(100))  # خروجی: 50.0

cart = ShoppingCart(NoDiscount())
print(cart.calculate_total(100))  # خروجی: 100.0