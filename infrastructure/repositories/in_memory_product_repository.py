from application.interfaces.product_repository_interface import IProductRepository
from domain.entities.product import Product
from typing import List, Optional

class InMemoryProductRepository(IProductRepository):

    def __init__(self):
        self.products = {
            1: Product(1, "Laptop", 2500, 10),
            2: Product(2, "Mouse", 50, 100),
            3: Product(3, "Keyboard", 120, 30)
        }

    def get_all(self) -> List[Product]:
        return list(self.products.values())

    def get_by_id(self, product_id: int) -> Optional[Product]:
        return self.products.get(product_id)

    def create(self, product: Product) -> Product:
        self.products[product.id] = product
        return product

    def update(self, product: Product) -> Product:
        self.products[product.id] = product
        return product

    def delete(self, product_id: int) -> bool:
        if product_id in self.products:
            del self.products[product_id]
            return True
        return False