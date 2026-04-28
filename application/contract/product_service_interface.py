from abc import ABC, abstractmethod
from typing import List
from domain.entities.product import Product
from application.dtos.product.create_product_dto import CreateProductDto
from application.dtos.product.update_product_dto import UpdateProductDto

class IProductService(ABC):

    @abstractmethod
    def get_all(self, page: int = 1, size: int = 10) -> List[Product]:
        pass

    @abstractmethod
    def get_by_id(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def create(self, dto: CreateProductDto) -> Product:
        pass

    @abstractmethod
    def update(self, product_id: int, dto: UpdateProductDto) -> Product:
        pass

    @abstractmethod
    def delete(self, product_id: int) -> bool:
        pass