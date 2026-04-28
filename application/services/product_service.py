from application.contract.product_service_interface import IProductService
from application.interfaces.product_repository_interface import IProductRepository
from application.mappers.product_mapper import ProductMapper
from shared.wappers.paginated_response import PaginatedResponse
from application.dtos.product.create_product_dto import CreateProductDto
from application.dtos.product.update_product_dto import UpdateProductDto
from application.dtos.product.product_response_dto import ProductResponseDto
from shared.exceptions.app_exception import AppException


class ProductService(IProductService):

    def __init__(self, repository: IProductRepository):
        self.repository = repository

    def get_all(self, page: int = 1, size: int = 10):
        products, total = self.repository.get_all(page, size)

        return PaginatedResponse[ProductResponseDto](
            items=[ProductMapper.to_response(p) for p in products],
            total=total,
            page=page,
            size=size
        )
    def get_by_id(self, product_id: int):
        product = self.repository.get_by_id(product_id)

        if not product:
            raise AppException("NOT_FOUND", "Product not found", 404)

        return product

    def create(self, dto: CreateProductDto):
        entity = ProductMapper.from_create_dto(dto)
        return self.repository.create(entity)

    def update(self, product_id: int, dto: UpdateProductDto):
        entity = self.repository.get_by_id(product_id)

        if not entity:
            raise AppException("NOT_FOUND", "Product not found", 404)

        entity = ProductMapper.update_entity(entity, dto)

        return self.repository.update(entity)

    def delete(self, product_id: int):
        return self.repository.delete(product_id)