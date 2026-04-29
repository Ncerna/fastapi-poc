from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from domain.entities.product import Product


class IProductRepository(ABC):

    @abstractmethod
    def get_all(self, page: int = 1, size: int = 10) -> Tuple[List[Product], int]:
        pass

    @abstractmethod
    def get_by_id(self, product_id: int) -> Optional[Product]:
        pass

    @abstractmethod
    def create(self, product: Product) -> Product:
        pass

    @abstractmethod
    def update(self, product: Product) -> Product:
        pass

    @abstractmethod
    def delete(self, product_id: int) -> bool:
        pass