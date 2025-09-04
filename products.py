

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def is_active(self) -> bool:
        return self.quantity > 0

    def activate(self):
        self.quantity = 1

    def deactivate(self):
        self.quantity = 0

    def show(self):
        print(f"{self.name}, Price: {self.price} Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        if self.quantity >= quantity:
            self.quantity -= quantity
            return self.price * quantity


