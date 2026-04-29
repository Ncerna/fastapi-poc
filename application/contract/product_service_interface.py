from abc import ABC, abstractmethod
from typing import List
from domain.entities.product import Product
from application.dtos.product.create_product_dto import CreateProductDto
from application.dtos.product.update_product_dto import UpdateProductDto
from application.shared.wappers.paginated_response import PaginatedResponse
from application.shared.wappers.response import ApiResponse

class IProductService(ABC):

    @abstractmethod
    def get_all(self, page: int = 1, size: int = 10) ->  PaginatedResponse:
        pass

    @abstractmethod
    def get_by_id(self, product_id: int) -> ApiResponse:
        pass

    @abstractmethod
    def create(self, dto: CreateProductDto) -> ApiResponse:
        pass

    @abstractmethod
    def update(self, product_id: int, dto: UpdateProductDto) -> ApiResponse:
        pass

    @abstractmethod
    def delete(self, product_id: int) -> ApiResponse:
        pass