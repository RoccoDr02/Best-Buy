from typing import List, Tuple
from products import Product


class Store:
    def __init__(self, products=None):
        if products is None:
            self.products = []
        else:
            self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Product '{product.name}' removed from the store.")
        else:
            print(f"Product '{product.name}' not found in the store.")

    def get_total_quantity(self) -> int:
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self) -> List['Product']:
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list: List[Tuple['Product', int]]) -> float:
        total = 0.0
        for product, quantity in shopping_list:
            if product in self.products and product.is_active():
                if product.get_quantity() >= quantity:
                    total += product.buy(quantity)
                else:
                    total += product.buy(product.get_quantity())
            else:
                print(f"Product '{product.name}' not available or inactive.")
        return total
