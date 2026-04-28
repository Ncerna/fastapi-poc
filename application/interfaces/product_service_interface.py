from abc import ABC, abstractmethod
from typing import List
from domain.entities.product import Product

class IProductService(ABC):

    @abstractmethod
    def get_all(self) -> List[Product]:
        pass

    @abstractmethod
    def get_by_id(self, product_id: int):
        pass

    @abstractmethod
    def create(self, product: Product):
        pass

    @abstractmethod
    def update(self, product: Product):
        pass

    @abstractmethod
    def delete(self, product_id: int):
        pass