import copy

class Prototype:
    def clone(self):
        # این متد برای کپی کردن شیء استفاده می‌شود.
        return copy.deepcopy(self)
    
class Product(Prototype):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(name={self.name}, price={self.price})"
    
# ساخت یک محصول اولیه
product1 = Product("Laptop", 1000)

# کپی کردن محصول اول
product2 = product1.clone()

# تغییر ویژگی‌های کپی شده
product2.name = "Smartphone"
product2.price = 500

# نمایش جزئیات هر محصول
print(product1)  # Output: Product(name=Laptop, price=1000)
print(product2)  # Output: Product(name=Smartphone, price=500)